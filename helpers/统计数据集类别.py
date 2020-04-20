from helpers.base_functions import count_pos_neg

train='data/AFQMC/train.csv'

df=count_pos_neg(train)

print('正例：',df[1],' 负例：',df[0])