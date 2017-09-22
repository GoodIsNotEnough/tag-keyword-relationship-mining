-- tmp_kgs_title_token;
load data local inpath '/home/kangguosheng/filetransfer/running_file' 
overwrite into table tmp_kgs_title_token partition(ds='2017-09-15');

DROP table  tmp_kgs_title_token;
CREATE TABLE if not exists tmp_kgs_title_token
(
char_id               STRING,
token          ARRAY<STRING>
) 
comment "title_token"
PARTITIONED BY (ds STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
COLLECTION ITEMS TERMINATED BY '\073'
MAP KEYS TERMINATED BY '\072'
STORED AS TEXTFILE;
-------------------------------------------------------------------------

-- tmp_kgs_title_token_tag
DROP table  tmp_kgs_title_token_tag;
CREATE TABLE if not exists tmp_kgs_title_token_tag
(
char_id               STRING,
token          ARRAY<STRING>,
tag               STRING  
) 
comment "title_token"
-- PARTITIONED BY (ds STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
COLLECTION ITEMS TERMINATED BY '\073'
MAP KEYS TERMINATED BY '\072'
STORED AS TEXTFILE;

INSERT INTO tmp_kgs_title_token_tag
SELECT 
t1.char_id,
t1.token,
t2.tag
FROM 
    (SELECT * 
    FROM tmp_kgs_title_token
    WHERE ds='2017-09-15'
    ) t1
LEFT JOIN
    (SELECT 
    sentence_id,
    tag    
    FROM idl_title_tag_agg
    WHERE ds='2017-09-12'
    AND start_day=0
    ) t2
ON t1.char_id=t2.sentence_id
WHERE t2.sentence_id IS NOT NULL;

SELECT count(1) --725972-->600510
FROM tmp_kgs_title_token_tag;
-------------------------------------------------------------------

-- tmp_kgs_tag_keyword_tfidf
DROP table  tmp_kgs_tag_keyword_tfidf;
CREATE TABLE if not exists tmp_kgs_tag_keyword_tfidf
(
tag               STRING,
keyword           STRING,
tfidf             FLOAT  
) 
comment "title_token"
PARTITIONED BY (ds STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
COLLECTION ITEMS TERMINATED BY '\073'
MAP KEYS TERMINATED BY '\072'
STORED AS TEXTFILE;

load data local inpath '/home/kangguosheng/filetransfer/tag_keyword_tfidf' 
overwrite into table tmp_kgs_tag_keyword_tfidf partition(ds='2017-09-19');
--------------------------------------------------------------------------

-- tmp_kgs_tag_keyword_stopwords
DROP table  tmp_kgs_tag_keyword_stopwords;
CREATE TABLE if not exists tmp_kgs_tag_keyword_stopwords
(
stopword     STRING
) 
comment "title_token"
-- PARTITIONED BY (ds STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
COLLECTION ITEMS TERMINATED BY '\073'
MAP KEYS TERMINATED BY '\072'
STORED AS TEXTFILE;

load data local inpath '/home/kangguosheng/filetransfer/all_stopwords.txt' 
overwrite into table tmp_kgs_tag_keyword_stopwords;


