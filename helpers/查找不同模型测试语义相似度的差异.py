from helpers.base_functions import find_difference_of_semantic_similarity

mapfile='data/003-50/标准问-相似问_4799.csv'
n=50
file1='m-base/'
file2='m-003.3-50-b0_epochs5_lr5e-5/'

find_difference_of_semantic_similarity(mapfile,n,file1,file2)