import os
import time

#在这里修改参数

task_name='sst'
do_train='true'
do_eval='true'
data_dir='/mnt/sda1/lca/bert-test/data/003'#训练集所在路径
vocab_file='/mnt/sda1/lca/chinese_L-12_H-768_A-12/vocab.txt'
bert_config_file='/mnt/sda1/lca/chinese_L-12_H-768_A-12/bert_config.json'
init_checkpoint='/mnt/sda1/lca/chinese_L-12_H-768_A-12/bert_model.ckpt'
max_seq_length=128
train_batch_size=16
learning_rate=5e-5
num_train_epochs=5.0
output_dir='/mnt/sda1/lca/bert-tuned-model/m-003.3-50-b0_epochs5_lr5e-5'#模型输出路径

#修改完成后执行脚本
t1=time.time()
os.system('source activate python36-lca && python /mnt/sda1/lca/bert-master/run_classifier.py --task_name={0} --do_train={1} --do_eval={2} --data_dir={3} --vocab_file={4} --bert_config_file={5} --init_checkpoint={6} --max_seq_length={7} --train_batch_size={8} --learning_rate={9} --num_train_epochs={10} --output_dir={11}'.format(task_name,do_train,do_eval,data_dir,vocab_file,bert_config_file,init_checkpoint,max_seq_length,train_batch_size,learning_rate,num_train_epochs,output_dir))
t2=time.time()
print('训练时间：',t2-t1,'s')