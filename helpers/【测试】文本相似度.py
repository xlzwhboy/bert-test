from helpers.base_functions import *

DISPLAY = True  # 是否打印
SAVE = True  # 是否保存
OUT_DIR = 'm-004_epochs3_lr2e-5'  # 语义相似度结果的输出文件夹，建议和使用的模型一致
TEST_TYPE = 0  # 1或0
# 1:run窗口执行，通过用户输入查询问题进行语义相似度匹配;
# 0：后台执行，通过读取指定文件的查询问题进行语义相似度匹配;
STANDARD_QUERY_FILE = '标准问666_2019-12.csv'  # 标准问库，用于匹配用户查询的问题
QUERY = load_user_query('相似问4797_2019-12.csv', 50)  # 用户查询问题(读取文件的前多少条)，仅在TEST_TYPE不为1时有效

if __name__ == '__main__':
    # 标准问库的句嵌入向量
    LIBRARY_EMBEDDING = []
    # 加载标准问库
    standard_query = load_standard_query(STANDARD_QUERY_FILE)
    # 获得标准问库的句嵌入向量
    LIBRARY_EMBEDDING = encode_sentence(standard_query)

    if TEST_TYPE == 1:
        while (True):
            print('----------------------------------------------')
            query = input(('请输入查询问题(输入0退出)：'))
            if query == '0':
                exit_here()
            query = query.split(',')
            # 用户查询问的句嵌入向量
            query_embedding = encode_sentence(query)
            # ’用户查询问的句嵌入向量‘与’标准问库的句嵌入向量‘的余弦相似度
            sim_list = calculate_SentenceEmbedding_similarity(query_embedding, LIBRARY_EMBEDDING)
            # 输出语义相似度结果
            display_text_similarity(query, standard_query, sim_list, display=DISPLAY, save=SAVE, out_dir=OUT_DIR)

    else:
        # 用户查询问的句嵌入向量
        query_embedding = encode_sentence(QUERY)
        # ’用户查询问的句嵌入向量‘与’标准问库的句嵌入向量‘的余弦相似度
        sim_list = calculate_SentenceEmbedding_similarity(query_embedding, LIBRARY_EMBEDDING)
        # 输出语义相似度结果
        display_text_similarity(QUERY, standard_query, sim_list, display=DISPLAY, save=SAVE, out_dir=OUT_DIR)
