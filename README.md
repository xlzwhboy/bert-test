# 语义匹配（文本相似度）测试
### 简要说明
使用Google Bert中文预训练模型在自己的数据集上进行微调，然后测试文本相似度（微调时使用句子对分类任务）
### 先决条件
- 了解如何使用Bert做文本（句子对）分类任务（其实就仿照Google的示例重写一下读取自己数据集的方式即可）
- 下载[Google Bert](https://github.com/google-research/bert)的中文预训练模型和源码用于微调
- 安装[hanxiao](https://github.com/hanxiao/bert-as-service#training-a-text-classifier-using-bert-features-and-tfestimator-api)大佬贡献的bert模型加载服务

