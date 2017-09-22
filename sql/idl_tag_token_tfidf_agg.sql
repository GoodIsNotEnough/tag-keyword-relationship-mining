-- 864181条记录
SELECT count(1)
from idl_tag_token_tfidf_agg;

DROP table  idl_tag_token_tfidf_agg;
CREATE TABLE if not exists idl_tag_token_tfidf_agg
(
tag               STRING,
keyword           STRING,
tfidf             FLOAT  
) 
comment "tag_token_tfidf 去长尾 去停用词"
PARTITIONED BY (ds STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
COLLECTION ITEMS TERMINATED BY '\073'
MAP KEYS TERMINATED BY '\072'
STORED AS TEXTFILE;

ALTER TABLE idl_tag_token_tfidf_agg DROP PARTITION (ds="2017-09-21");
INSERT INTO idl_tag_token_tfidf_agg PARTITION (ds="2017-09-21")
SELECT
t1.tag,
t1.keyword,
t1.tfidf
FROM tmp_kgs_tag_keyword_tfidf_filter t1
LEFT JOIN tmp_kgs_tag_keyword_stopwords t2
ON t1.keyword=t2.stopword
WHERE t2.stopword IS NULL;

SELECT --194910-34138=160772 actual:160873
count(DISTINCT keyword)
FROM idl_tag_token_tfidf_agg;

SELECT --5.371821250303034
count(1)/count(DISTINCT keyword)
FROM idl_tag_token_tfidf_agg;

CREATE TABLE tmp_kgs_tag_keyword_maxTimeInTag AS
SELECT
keyword,
count(1) as TimeInTag
FROM idl_tag_token_tfidf_agg
GROUP BY keyword
ORDER BY TimeInTag DESC;

