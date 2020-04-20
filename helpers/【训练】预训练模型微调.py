import os
import time

# 定义路径
bert_master_path = '/mnt/sda1/lca/bert-master/'  # google bert源码的路径
bert_test_path = '/mnt/sda1/lca/bert-test/'  # bert-test的路径
bert_pre_trained_model_path = '/mnt/sda1/lca/chinese_L-12_H-768_A-12/'  # 谷歌中文预训练模型的路径
bert_tuned_model_path = '/mnt/sda1/lca/bert-tuned-model/'  # 微调模型的保存路径

# 在这里修改参数
task_name = 'sst'  # semantic similarity task 语义相似度任务
do_train = 'true'
do_eval = 'true'
data_dir = bert_test_path + 'data/004'  # 训练语料所在路径，至少包含train.csv和dev.csv
vocab_file = bert_pre_trained_model_path + 'vocab.txt'
bert_config_file = bert_pre_trained_model_path + 'bert_config.json'
init_checkpoint = bert_pre_trained_model_path + 'bert_model.ckpt'
max_seq_length = 128
train_batch_size = 16
learning_rate = 2e-5
num_train_epochs = 8.0
output_dir = bert_tuned_model_path + 'm-004_epochs8_lr2e-5'  # 模型输出路径

# 修改完成后执行脚本
t1 = time.time()
# source activate python36-lca表示在虚拟环境python36-lca下执行该命令，按需修改；若不在虚拟环境下，删除&&及之前的命令即可
os.system(
    'source activate python36-lca && python {0}run_classifier.py --task_name={1} --do_train={2} --do_eval={3} --data_dir={4} --vocab_file={5} --bert_config_file={6} --init_checkpoint={7} --max_seq_length={8} --train_batch_size={9} --learning_rate={10} --num_train_epochs={11} --output_dir={12}'.format(
        bert_master_path, task_name, do_train, do_eval, data_dir, vocab_file, bert_config_file, init_checkpoint,
        max_seq_length, train_batch_size, learning_rate, num_train_epochs, output_dir))
t2 = time.time()
print('训练时间：', t2 - t1, 's')
