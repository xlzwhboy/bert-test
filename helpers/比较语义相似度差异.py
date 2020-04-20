from helpers.base_functions import find_difference_of_semantic_similarity

mapfile='data/query repositories/标准问-相似问_4799.csv'#建立标准问与相似问映射的数据集，形式为｛相似问1：标准问1｝
n=50#取数据集前多少条建立该映射

#模型1和模型2需要对相同的用户查询问题进行测试，语义相似度的测试结果保存在对应的路径下
model1= 'm-base'#模型1的语义相似度的测试结果所在文件夹
model2= 'm-004_epochs3_lr5e-5'#模型2的语义相似度的测试结果所在文件夹

#比较模型1和模型2的测试结果的差异
find_difference_of_semantic_similarity(mapfile, n, model1, model2)