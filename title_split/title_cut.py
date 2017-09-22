#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os
from jieba_cut import *
import string
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def running_task(taskfile,running_file,api):
  if not os.path.exists(taskfile):
    input_file_tag = -1
    print taskfile,'does not exist!!!'
  else:
    input_file_data = open(taskfile, "r")
    input_file_tag = 1
  length=0
  result_num=0
  if input_file_tag==1:
    if not os.path.exists(running_file):
      result_data=open(running_file,"w") #若文件不存在,则创建
      result_data.close()
    while True:
      full_line=input_file_data.readline()
      if not full_line:
        break
      full_line=full_line.strip().encode('utf-8')
      split_list=full_line.split(unicode(',','utf-8'))
      char_id=split_list[0]
      char_raw=split_list[1]
      seg_list = seg_sentence(char_raw)  
      seg_list = list(set(seg_list)) #去重
      length=length+len(seg_list)
      output_text=(char_id+','+';'.join(seg_list)).encode("utf-8")+'\n'
      result_data = open(running_file, "a")
      result_data.write(output_text)
      result_data.close()
      result_num+=1
  print "There are %d lines in the resulted running_file !!!" % result_num
  print length #所有关键词总数
  print float(length)/300000
