项目背景:
各商品的描述组成句子,因此尤其对应的关键词.各商品又有个字的标签.

项目技术:TF-IDF
TF:关键词在tag中出现的频率
IDF:log(所有的句子数目/(包含关键词的句子数目+1))

项目目标:
挖掘标签与关键词之间的关系.

技术路线:
Step1:从idl_title_agg表中抽取300000商品描述的句子进行分词;
Step2:将商品和tag联系起来,输出sample_300000_token_tag;
Step3:计算keyword与tag之间的tfidf值,得到表tmp_kgs_tag_keyword_tfidf;
Step4:根据keyword在tag中的出现次数及词本身的无含义特征,抽取出停用词;
Step5:对每个keyword去掉tag长尾,并去掉停用词.
