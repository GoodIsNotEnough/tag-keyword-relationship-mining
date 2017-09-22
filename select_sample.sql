-- 抽取300000个物品描述的句子
insert overwrite local directory '/home/kangguosheng/tmp'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY '\073'
MAP KEYS TERMINATED BY '\072'
STORED AS TEXTFILE
select *
from idl_title_agg
order by rand()
limit 300000;

-- 抽取300000个物品的分词列表及关联的tag列表
insert overwrite local directory '/home/kangguosheng/tmp'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY '\073'
MAP KEYS TERMINATED BY '\072'
STORED AS TEXTFILE
select
char_id,
token,
collect_set(tag) AS tag_list
from tmp_kgs_title_token_tag
group by char_id,token;

-- 抽取所有关键词及出现在tag中的次数
insert overwrite local directory '/home/kangguosheng/tmp'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY '\073'
MAP KEYS TERMINATED BY '\072'
STORED AS TEXTFILE
SELECT
keyword,
count(1)
FROM tmp_kgs_tag_keyword_tfidf
group by keyword;