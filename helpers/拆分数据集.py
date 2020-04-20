from helpers.base_functions import split_dataset

#要拆分的数据集请命名为alldata.csv
DATA_PATH='data/004/'#alldata.csv数据集所在路径

#按指定比例拆分alldata.csv数据集为train.csv.dev.csv,test.csv
split_dataset(8,2,0,DATA_PATH)#例如(10,1,1,DATA_PATH)表示按10:1:1拆分为train,dev,test