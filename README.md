# 语义匹配（文本相似度）测试
### 简要说明
使用Google Bert中文预训练模型在自己的数据集上进行微调，然后测试文本相似度（微调时使用句子对分类任务）
### 先决条件
- 了解如何使用Bert做文本（句子对）分类任务（其实就仿照Google的示例重写一下读取自己数据集的方式即可）
- 下载[Google Bert](https://github.com/google-research/bert)的中文预训练模型和源码用于微调
- 安装[hanxiao](https://github.com/hanxiao/bert-as-service#training-a-text-classifier-using-bert-features-and-tfestimator-api)大佬贡献的bert模型加载服务
### 脚本功能

- 【训练】在Google Bert中文预训练模型的基础上微调
- 【启动】加载已经训练好的模型文件，将模型作为一个服务提供出来
- 【测试】语义匹配测试，输入查询问题、匹配标准问库，给出相似度排序  
此外还有其他脚本
- 拆分数据集：将数据集按固定比例随机采样拆分为3个：train、dev、test
- 统计数据集类别：输入数据集，统计类别分布
- 查找不同模型测试语义相似度的差异：如果需要比较两次训练的模型对于语义匹配结果的差异，可以使用此脚本
