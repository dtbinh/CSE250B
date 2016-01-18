import numpy as np
import scipy as sp

def calculate_pi_j(dada, label):
    pij = np.zeros((20,1))

    for i in range(1, 21):
        index = np.extract(label == i, label)
        pij[i-1] = index.shape[0]

    total = np.sum(pij)
    pij = pij / total
    return pij

def calculate_pj_w(train_data, train_label):
    data = np.array(train_data)
    doc_id = data[:, 0]
    word_id = data[:,1]
    count = data[:, 2]
    word_num = np.max(word_id)
    doc_num = np.max(doc_id)

    pjw = np.zeros((20, word_num), 'int64')

    for i in range(0, doc_id.shape[0]):
        label = train_label[doc_id[i] - 1] - 1
        word_index = word_id[i] - 1
        pjw[label, word_index] += count[i]
    return pjw

def 



if __name__ == '__main__':
    # Load training data
    data_dir = 'C:\\Users\\bisai\\Documents\\GitHub\\CSE250B\\data\\20news-bydate\\matlab\\'
    print 'Load training data...'
    train = np.loadtxt('%strain.data'%data_dir)
    print 'Load training label...'
    train_label = np.loadtxt('%strain.label'%data_dir)
    # pij = calculate_pi_j(train, train_label)
    # print
    pjw = calculate_pj_w(train, train_label)
    np.save('%spjw'%data_dir, pjw)
