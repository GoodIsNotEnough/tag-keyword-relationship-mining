
#-*-coding:utf-8-*-
import sys
import pprint
reload(sys)
sys.setdefaultencoding('utf8')
import datetime
import numpy as np
# from sklearn.multiclass import OneVsRestClassifier
from sklearn import linear_model

def load_dict(dict_file_name):
    dict_file = file(dict_file_name,'r')
    loaded_dict = {}
    i = 0
    while True:
        char0 = dict_file.readline()
        char = unicode(char0.strip('\n\r'), "utf-8")
        if not char:
            break
        loaded_dict[char] = i
        i += 1
    print "length", dict_file_name, len(loaded_dict)
    return loaded_dict

def generate_matrix(keyword_dict, tag_dict, source_file):
    matrix_x = []
    matrix_y = []
    while True:
        char0 = source_file.readline()
        chars = unicode(char0.strip('\n\r'), "utf-8")
        if not chars:
            break
        char_list = chars.split(',')
        # pid = char_list[0]
        keyword_list = char_list[1].split(';')
        tag_list = char_list[2].split(';')
        v_keywords = np.zeros(len(keyword_dict))
        v_tags = np.zeros(len(tag_dict))
        #在向量相应keyword的位置上替换上1
        for i in keyword_list:
            if keyword_dict.has_key(i):
                v_keywords[keyword_dict[i]] = 1
        for j in tag_list:
            if tag_dict.has_key(j):
                v_tags[tag_dict[j]] = 1
        matrix_x.append(v_keywords)
        matrix_y.append(v_tags)
    # np.savetxt(open('matrix_y', 'w'), matrix_y, delimiter=',')
    print 'generate_matrix finished'
    return matrix_x, matrix_y

def generate_ovr(X, matrix_y, sample_num):
    print "begin LR"
    i = matrix_y.shape[1]
    # parameter_combined = np.array([])
    # f = file('in_case_does_not_work', 'w')
    file_name = 'parameter_0809_'+str(sample_num)
    new_f = open(file_name,'w')
    print "i:", i
    for j in range(i):
        print "tag no.:", j
        y = matrix_y[:,j]
        print "shape y:", y.shape
        print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lgt = linear_model.LogisticRegression(penalty='l1', n_jobs=-1, C=1.0, fit_intercept=False, solver='liblinear',\
                                              class_weight='balanced', max_iter=500)
        # print "begin OVR"
        # classif = OneVsRestClassifier(lgt, n_jobs=-1)
        classif = lgt
        # 训练分类器
        print "begin fit"
        classif.fit(X, y)
        print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        parameter = classif.coef_
        print parameter[:100]
        # parameter_combined = np.hstack((parameter_combined, parameter))
        np.savetxt(open(file_name, 'a'), parameter, delimiter=',')
        # new_f.write('\n')
    print "begin saving file:", file_name
    new_f.close()
    print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def do_lr():
    print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    keyword_file_name = 'keywords.txt'
    tag_file_name = 'tags.txt'
    keyword_dict = load_dict(keyword_file_name)
    tag_dict = load_dict(tag_file_name)
    for sample_num in range(1, 10):
        print "="*100
        print "This is the %d of Ten model" % (sample_num)
        source_file = file('sample_0809_'+str(sample_num), 'r')
        matrix_x, matrix_y = generate_matrix(keyword_dict, tag_dict, source_file)
        matrix_x = np.matrix(matrix_x)
        matrix_y = np.matrix(matrix_y)
        reduction_matrix = np.load('reduction_mat.npy')
        print "reduction_matrix loaded"
        print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        X = matrix_x * reduction_matrix
        print "X generated"
        print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        generate_ovr(X, matrix_y, sample_num)
        print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

do_lr()

#最后将10个结果矩阵取平均

'''
X : (sparse) array-like, shape = [n_samples, n_features]
y : (sparse) array-like, shape = [n_samples, n_classes]
Multi-class targets. An indicator matrix turns on multilabel classification.
'''