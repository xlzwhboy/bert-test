import os

#在这里修改参数

model_dir='/mnt/sda1/lca/chinese_L-12_H-768_A-12'
tuned_model_dir='/mnt/sda1/lca/bert-tuned-model/m-003.3-50-b0_epochs5_lr5e-5'#微调模型路径
ckpt_name='model.ckpt-44'#微调模型保存时的ckpt名,数字为global_step
use_tuned=1#是否加载微调模型；1表示加载，需要指定微调模型路径；0表示仅启动谷歌中文预训练模型

#修改完成后执行脚本

if use_tuned==1:
    os.system('source activate python36-lca && bert-serving-start -model_dir={0} -tuned_model_dir={1} -ckpt_name={2}'.format(model_dir,tuned_model_dir,ckpt_name))
else:
    os.system('source activate python36-lca && bert-serving-start -model_dir={0}'.format(model_dir))