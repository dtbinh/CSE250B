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
    # word_num = np.max(word_id)
    word_num = 61188
    doc_num = np.max(doc_id)

    pjw = np.zeros((20, word_num), 'int64')

    for i in range(0, doc_id.shape[0]):
        label = train_label[doc_id[i] - 1] - 1
        word_index = word_id[i] - 1
        pjw[label, word_index] += count[i]
    return pjw

def test(test_data, test_label, train_pj, train_pjw):
    pj = np.log(train_pj)
    count = np.sum(train_pjw, 1) + 61188
    count = np.array(count, 'float64')
    pjw = (train_pjw + 1) / count[:, None]
    pjw = np.log(pjw)


    test_num = np.max(test_data[:, 0])
    doc_id = test_data[:, 0]
    word_id = test_data[:,1]
    word_count = test_data[:,2]

    word_num = 61188
    error_count = 0
    for i in range(0, int(test_num)):
        index = np.where(doc_id == i + 1)
        freq = np.zeros(word_num)

        freq[word_id[index]-1] = word_count[index]

        total = np.sum(word_count[index])
        # freq = freq / total

        error = np.zeros((20, 1))
        for j in range(0, 20):
            temp = np.multiply(freq, pjw[j, :])
            error[j] = np.sum(temp) + pj[j]
        index = np.argmax(error)
        if index != test_label[i] - 1:
            error_count = error_count + 1

    print error_count / float(test_num)









if __name__ == '__main__':
    # Load training data
    data_dir = 'C:\\Users\\bisai\\Documents\\GitHub\\CSE250B\\data\\20news-bydate\\matlab\\'
    # print 'Load training data...'
    # train = np.loadtxt('%strain.data'%data_dir)
    # print 'Load training label...'
    # train_label = np.loadtxt('%strain.label'%data_dir)
    # pij = calculate_pi_j(train, train_label)
    # np.save('%spj'%data_dir, pij)
    # pjw = calculate_pj_w(train, train_label)
    # np.save('%spjw'%data_dir, pjw)
    # exit(-1)

    pj = np.load('%spj.npy'%data_dir)
    pjw = np.load('%spjw.npy'%data_dir)
    print 'Load test data...'
    test_data = np.loadtxt('%stest.data'%data_dir, 'int')
    print 'Load test label...'
    test_label = np.loadtxt('%stest.label'%data_dir, 'int')

    test(test_data,test_label,pj, pjw)
