��Ŀ����:
����Ʒ��������ɾ���,��������Ӧ�Ĺؼ���.����Ʒ���и��Եı�ǩ.

��Ŀ����:
TF-IDF

��ĿĿ��:
�ھ��ǩ��ؼ���֮��Ĺ�ϵ

����·��:
��Step1��:��idl_title_agg���г�ȡ300000��Ʒ�����ľ��Ӳ��ý�ͽ��зִ�;
Դ�����title_split�ļ���
ע:ɾ�����ԭ�дʿ�,�����Լ��Ĵʿ�
#�滻��ʹʿ�
dcit_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'dict.txt')
jieba.set_dictionary(dcit_path)
��Step2��:����Ʒ��tag��ϵ����,���sample_300000_token_tag;
��Step3��:����keyword��tag֮���tfidfֵ,�õ���tmp_kgs_tag_keyword_tfidf;
��Step4��:����keyword��tag�еĳ��ִ������ʱ�����޺�������,��ȡ��ͣ�ô�;
��Step5��:��ÿ��keywordȥ��tag��β,��ȥ��ͣ�ô�.

��:��Ʒ&�û���ǩ�����title_user_tag�ļ���