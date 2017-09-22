#!/usr/bin/python
# -+- coding: utf-8 -+-
import re,os
import sys,math
import string
import datetime
import time
reload(sys)
sys.setdefaultencoding('utf-8')
starttime = datetime.datetime.now()    
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

fin_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "sample_300000_token_tag")
fin=open(fin_path) #打开文件
keyword2num=dict()
tag2keyword=dict()
sentence_num=0
for line in fin:
  sentence_num+=1
  line=unicode(line.strip(),'utf-8')
  setence_id,tokens,tags=line.split(unicode(',','utf-8'))
  keyword_list=tokens.split(unicode(';','utf-8'))
  tag_list=tags.split(unicode(';','utf-8'))
  for keyword in keyword_list:
    keyword2num[keyword]=keyword2num.get(keyword,0)+1
  for tag in tag_list:
    if tag2keyword.has_key(tag):
      tag2keyword[tag].extend(keyword_list)
    else:
      tag2keyword[tag]=keyword_list
fin.close()
print 'there are %d senteces!!!' % sentence_num
print 'there are %d keywords in all sentences!!!' % len(keyword2num)
print 'there are %d tags for all sentences!!!' % len(tag2keyword)

# fout_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "keywords")
# fout=open(fout_path,'w') #打开文件
# for keyword in keyword2num:
#   fout.write(keyword.encode('utf-8')+'\n')
# fout.close()

keyword2idf=dict()
for keyword in keyword2num:
  keyword2idf[keyword]=math.log(float(sentence_num)/(keyword2num[keyword]+1))

fout_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "tag_keyword_tfidf")
fout=open(fout_path,'w') #打开文件
tag_no=0;
for tag in tag2keyword:
  tag_no+=1
  keyword2tfidf=dict()
  keywords=set(tag2keyword[tag]) #tag关联的keywords
  length=len(tag2keyword[tag])
  print "tag_%d: %s(keywords:%d) is processing... elapsed time %s ..."%(tag_no,tag.encode('utf-8'),len(keywords),(datetime.datetime.now() - starttime))
  for keyword in keywords:
    tf=float(tag2keyword[tag].count(keyword))/length
    idf=keyword2idf[keyword]
    tf_idf=tf*idf
    keyword2tfidf[keyword]=tf_idf
  sorted_dict=sorted(keyword2tfidf.iteritems(), key=lambda d:d[1], reverse = True ) #d[0]为key,d[1]为value,返回一个元组列表
  # need_num=int(len(sorted_dict)*0.5) #50%
  for keyword,tfidf in sorted_dict:
    new_line=','.join([tag,keyword,str(tfidf)])
    fout.write(new_line.encode('utf-8')+'\n')
fout.close()

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 