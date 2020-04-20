from helpers.base_functions import *

DISPLAY=True#是否打印
SAVE=True#是否保存
OUT_DIR='m-003.3-50-b0_epochs5_lr5e-5'#文本相似度结果保存目录，非必须
TEST_TYPE=0#1:在run窗口持续运行;否则执行一次
STANDARD_QUERY_FILE='标准问666_2019-12.csv'#标准问库
QUERY=load_user_query_from_train('003-50/标准问-相似问_4799.csv',50)#用户查询问题，如有多个问题在列表里添加，仅在TEST_TYPE不为1时有效

if __name__ == '__main__':
    # 标准语句库的句嵌入向量
    LIBRARY_EMBEDDING = []
    # 加载标准语句库
    standard_query=load_standard_query(STANDARD_QUERY_FILE)
    #获得标准语句库的句嵌入向量
    LIBRARY_EMBEDDING=encode_sentence(standard_query)

    if TEST_TYPE==1:
        while(True):
            print('----------------------------------------------')
            query=input(('请输入查询问题(输入0退出)：'))
            if query=='0':#用户输出0，退出
                exit_here()
            query=query.split(',')
            #用户查询的句嵌入向量
            query_embedding=encode_sentence(query)
            #’用户查询的句嵌入向量‘与’标准语句库的句嵌入向量‘的余弦相似度
            sim_list=calculate_SentenceEmbedding_similarity(query_embedding,LIBRARY_EMBEDDING)
            #输出文本相似度结果
            display_text_similarity(query, standard_query, sim_list, display=DISPLAY, save=SAVE, out_dir=OUT_DIR)

    else:
        # 用户查询的句嵌入向量
        query_embedding = encode_sentence(QUERY)
        # ’用户查询的句嵌入向量‘与’标准语句库的句嵌入向量‘的余弦相似度
        sim_list = calculate_SentenceEmbedding_similarity(query_embedding, LIBRARY_EMBEDDING)
        # 输出文本相似度结果
        display_text_similarity(QUERY, standard_query, sim_list, display=DISPLAY, save=SAVE, out_dir=OUT_DIR)