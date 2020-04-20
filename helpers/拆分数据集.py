from helpers.base_functions import split_dataset

dataset='alldata.csv'#要拆分的数据集
DATA_PATH='data/004/'#alldata.csv数据集所在路径

#按指定比例拆分alldata.csv数据集为train.csv.dev.csv,test.csv
split_dataset(8,2,0,dataset,DATA_PATH)#例如(10,1,1,DATA_PATH)表示按10:1:1拆分为train,dev,test