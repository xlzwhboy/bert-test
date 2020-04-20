from helpers.base_functions import split_dataset

DATA_PATH='../data/'#数据集路径
dir='001/'#数据集所在文件夹名

#按10:1:1拆分alldata.csv数据集为train.csv,dev.csv,test.csv
split_dataset(DATA_PATH+dir)