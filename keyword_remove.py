#!/usr/bin/python
# -+- coding: utf-8 -+-
import re,os
import sys,math
import string
reload(sys)
sys.setdefaultencoding('utf-8')

def isPunctuation(keywords): #判断是否是由英文标点符号组成的字符串
  punctuation=string.punctuation+' '
  for word in keywords:
    if word not in punctuation:
      return False
  return True

stopwords_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "stopwords.txt")
stopwords_fin=open(stopwords_path) #打开文件
stopwords=[]
for line in stopwords_fin:
  line=unicode(line.strip(),'utf-8')
  stopwords.append(line)
stopwords_fin.close()
print "there are %d stopwords already!!!"%len(stopwords)

fin_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "keywords_timesInTag")
fin=open(fin_path) #打开文件
fout_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "removed_keywords.txt")
fout=open(fout_path,'w') #打开文件
fout.close()

digital_letter_reg=r'^(\w+)$'
digital_letter_reg=re.compile(unicode(digital_letter_reg,'utf8'))
chinese_reg=ur'^([\u4e00-\u9fa5])$' #注意:汉字的范围
chinese_reg=re.compile(chinese_reg)

for line in fin:
  line=unicode(line.strip(),'utf-8')
  field_list=line.split(unicode(',','utf-8'))
  keyword=field_list[0]
  appear_time=int(field_list[1])
  result=re.search(digital_letter_reg,keyword) #匹配是否是字母/数字构成的字符串
  if result is not None and appear_time<=5:
    fout=open(fout_path,'a') #打开文件
    fout.write(keyword.encode('utf-8')+'\n')
    fout.close()
  if len(keyword)==1: #keyword长度为1
    result=re.search(chinese_reg,keyword) #匹配是否是汉字
    if result is None and keyword not in stopwords: #不是汉字
      fout=open(fout_path,'a') #打开文件
      fout.write(keyword.encode('utf-8')+'\n')
      fout.close()
  else:
    if isPunctuation(keyword):
      fout=open(fout_path,'a') #打开文件
      fout.write(keyword.encode('utf-8')+'\n')
      fout.close()

fin.close()
fout.close()

