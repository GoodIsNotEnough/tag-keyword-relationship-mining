项目背景:
各商品的描述组成句子,因此尤其对应的关键词.各商品又有各自的标签.

项目技术:
TF-IDF

项目目标:
挖掘标签与关键词之间的关系

技术路线:
【Step1】:从idl_title_agg表中抽取300000商品描述的句子采用结巴进行分词;
源代码见title_split文件夹
注:删除结巴原有词库,采用自己的词库
#替换结巴词库
dcit_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'dict.txt')
jieba.set_dictionary(dcit_path)
【Step2】:将商品和tag联系起来,输出sample_300000_token_tag;
【Step3】:计算keyword与tag之间的tfidf值,得到表tmp_kgs_tag_keyword_tfidf;
【Step4】:根据keyword在tag中的出现次数及词本身的无含义特征,抽取出停用词;
【Step5】:对每个keyword去掉tag长尾,并去掉停用词.

附:商品&用户标签画像见title_user_tag文件夹