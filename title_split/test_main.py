# coding=utf-8
__author__ = 'kangguosheng'

import os,sys
from list_operate import *
from title_cut import *
reload(sys)
sys.setdefaultencoding('utf8')
taskfile=os.path.join(os.getcwd(), "sample_300000_sentence")
runningfile=os.path.join(os.getcwd(), "running_file")
api='not exist'
running_task(taskfile, runningfile, api)
