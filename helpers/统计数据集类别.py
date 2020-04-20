from helpers.base_functions import count_pos_neg

train='data/004/train.csv'#要统计类别分布的数据集

df=count_pos_neg(train)

print('正例：',df[1],' 负例：',df[0])