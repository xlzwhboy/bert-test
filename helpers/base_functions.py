import numpy as np
import pandas as pd
import os
import time
from bert_serving.client import BertClient
from termcolor import colored

import warnings

warnings.filterwarnings("ignore")

os.chdir('../')  # 设置当前目录为项目根目录


def cosine_similarity(x, y, norm=False):
    """ 计算两个向量x和y的余弦相似度 """
    assert len(x) == len(y), "len(x) != len(y)"

    if (x == y).any():
        return 1.0

    res = np.array([[x[i] * y[i], x[i] * x[i], y[i] * y[i]] for i in range(len(x))])
    cos = sum(res[:, 0]) / (np.sqrt(sum(res[:, 1])) * np.sqrt(sum(res[:, 2])))

    return 0.5 * cos + 0.5 if norm else cos  # 归一化到[0, 1]区间内


def split_dataset(a,b,c,dataset_dir):
    '''按a:b:c拆分数据集为train,dev,test'''
    df_all = pd.read_csv(dataset_dir + 'alldata.csv', header=None)
    # 拆分出训练集train
    df_train = df_all.sample(frac=a/(a+b+c))
    # 剩下
    df_remain = df_all[~df_all.index.isin(df_train.index)]
    # 拆分出验证集dev
    df_dev = df_remain.sample(frac=b/(b+c))
    if(c!=0):
        # 剩下为测试集test
        df_test = df_remain[~df_remain.index.isin(df_dev.index)]
        df_test.to_csv(dataset_dir + 'test.csv', header=None, index=False)
    # 保存到文件
    df_train.to_csv(dataset_dir + 'train.csv', header=None, index=False)
    df_dev.to_csv(dataset_dir + 'dev.csv', header=None, index=False)



def load_standard_query(inputfile):
    '''加载标准问库'''
    df = pd.read_csv('data/query repositories/' + inputfile, header=None)
    return df[0].values.tolist()


def load_user_query(inputfile, n):
    '''加载用户查询问题'''
    df = pd.read_csv('data/query repositories/' + inputfile, header=None)
    return df.head(n)[0].values.tolist()


def encode_sentence(sentence_list):
    '''获得句嵌入向量'''
    return BertClient().encode(sentence_list)  # ip='192.168.1.3',show_server_config=True


def calculate_SentenceEmbedding_similarity(sentence_embedding1, sentence_embedding2):
    '''计算句嵌入向量余弦相似度'''

    sim_list = []

    for se1 in sentence_embedding1:
        temp_list = []
        for se2 in sentence_embedding2:
            temp_list.append(cosine_similarity(se1, se2))
        sim_list.append(temp_list)

    return sim_list


def display_text_similarity(query, library, sim_list, display=True, save=False, out_dir=None):
    '''展示文本相似度结果'''

    out_dir = 'output/' + out_dir if out_dir is not None else 'output/temp'

    for idx, elem in enumerate(query):
        df = pd.DataFrame({
            '语句': library,
            '相似度': sim_list[idx]
        }).sort_values(by='相似度', ascending=False)
        df = df.reset_index(drop=True)
        if display:
            print(('用户查询：'))
            print('\t', elem)
            print(('匹配结果：'))
            print(df.head(10))

        if save:
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
            name = elem.replace('/', 'or')
            name = name[:10] if len(name) > 10 else name

            df0 = pd.DataFrame({
                '语句': [elem],
                '相似度': [1.0]
            })
            df = df0.append(df).reset_index(drop=True)
            df.to_csv(out_dir + '/' + name + '.csv', header=None)


def count_pos_neg(inputfile):
    '''统计正例负例'''
    return pd.read_csv(inputfile, header=None)[2].value_counts()


def find_difference_of_semantic_similarity(mapfile, n, model1, model2):
    '''查找不同模型语义相似度测试结果的差异'''
    map = {}
    df0 = pd.read_csv(mapfile, header=None).head(n)
    for row in df0.itertuples():
        # map[row[1]]=row[2]
        map[row[2]] = row[1]

    path = 'output/'

    files1 = os.listdir(path + model1)
    # files2 = os.listdir(path + model2)

    df_res = pd.DataFrame(columns=['标准问', '相似问', '相似度'+model1, '相似度'+model2, '排名'+model1, '排名'+model2])
    query_sta = []
    query_sim = []
    sim_base_list = []
    sim_tuned_list = []
    rank_base_list = []
    rank_tuned_list = []

    for file in files1:
        df1 = pd.read_csv(path + model1 + file, header=None)
        df2 = pd.read_csv(path + model2 + file, header=None)
        s1 = ''
        s2 = ''
        sim_base = -1.0
        sim_tuned = -1.0
        rank_base = -1
        rank_tuned = -1
        # file1's file
        for row1 in df1.itertuples():
            if row1[1] == 0:
                s1 = row1[2]
                s2 = map[row1[2]]
                continue
            if row1[2] == s2:
                sim_base = row1[3]
                rank_base = row1[1]
                break
        # file2's file
        for row2 in df2.itertuples():
            if row2[1] == 0:
                continue
            if row2[2] == s2:
                sim_tuned = row2[3]
                rank_tuned = row2[1]
                break
        query_sim.append(s1)
        query_sta.append(s2)
        sim_base_list.append(sim_base)
        sim_tuned_list.append(sim_tuned)
        rank_base_list.append(rank_base)
        rank_tuned_list.append(rank_tuned)

    df_res = df_res.append(pd.DataFrame(
        {'标准问': query_sta, '相似问': query_sim, '相似度'+model1: sim_base_list, '相似度'+model2: sim_tuned_list,
         '排名'+model1: rank_base_list, '排名'+model2: rank_tuned_list}))
    # df_res.columns = [['句子对', '句子对', '相似度', '相似度', '排名', '排名'], ['标准问', '相似问/查询问', model1, model2, model1, model2]]
    outputfile = 'output/语义相似度差异表'

    currenttime = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime())

    # df_res=df_res.round(4)
    # df_res.sort_values(['句子对','标准问'], inplace=True)
    df_res = df_res.reset_index(drop=True)
    df_res.index.name = '序号'
    df_res.to_csv(outputfile + '-' + currenttime + '.csv')


def exit_here():
    os._exit(0)
