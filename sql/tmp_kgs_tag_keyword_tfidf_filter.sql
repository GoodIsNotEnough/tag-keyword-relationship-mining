tmp_kgs_tag_keyword_tfidf_yj01

CREATE TABLE tmp_kgs_tag_keyword_tfidf_filter AS
SELECT tag,
       keyword,
       tfidf,
       tfidf_t,
       tfidf_c,
       tfidf_c/tfidf_t AS tfidf_ratio
FROM
  (SELECT tag,
          keyword,
          tfidf,
          SUM(tfidf)OVER(Partition BY keyword) AS tfidf_t,
          SUM(tfidf)OVER(Partition BY keyword
                         ORDER BY ranks) AS tfidf_c
   FROM
     (SELECT tag,
             keyword,
             tfidf,
             row_number()over(Partition BY keyword
                              ORDER BY tfidf) AS ranks
      FROM tmp_kgs_tag_keyword_tfidf
      ) a1
  ) t1
WHERE tfidf_c/tfidf_t>0.1;

SELECT --194910
count(DISTINCT keyword)
FROM tmp_kgs_tag_keyword_tfidf_filter;

SELECT *
from idl_tag_token_tfidf_agg
WHERE keyword='年货';
