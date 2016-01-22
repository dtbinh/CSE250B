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
    # doc_num = np.max(doc_id)
    # doc_num = train_label.shape[0]

    pjw = np.zeros((20, word_num), 'int64')

    for i in range(0, doc_id.shape[0]):
        label = train_label[doc_id[i] - 1] - 1
        word_index = word_id[i] - 1
        pjw[label, word_index] += count[i]
    return pjw

def test(test_data, test_label, train_pj, train_pjw, word_weight = 1.0):
    pj = np.log(train_pj)
    count = np.sum(train_pjw, 1) + 61188
    count = np.array(count, 'float64')
    pjw = (train_pjw + 1) / count[:, None]
    pjw = np.log(pjw)
    # pjw = np.log(1 + pjw)

    # test_num = np.max(test_data[:, 0])
    # test_num = test_label.shape[0]
    test_doc_id = np.unique(test_data[:, 0])
    test_num = test_doc_id.shape[0]

    doc_id = test_data[:, 0]
    word_id = test_data[:, 1]
    word_count = test_data[:,2]

    word_num = 61188
    error_count = 0
    for i in range(0, int(test_num)):
        # index = np.where(doc_id == i + 1)
        index = np.where(doc_id == test_doc_id[i])
        freq = np.zeros(word_num)

        freq[word_id[index]-1] = word_count[index]

        total = np.sum(word_count[index])
        # freq = freq / total
        # freq = np.log(1.0 + freq)
        freq = np.multiply(word_weight.transpose(), freq)
        error = np.zeros((20, 1))
        for j in range(0, 20):
            temp = np.multiply(freq, pjw[j, :])
            error[j] = np.sum(temp) + pj[j]
        # error = freq * pjw.transpose() + pj
        index = np.argmax(error)
        if index != test_label[test_doc_id[i]-1] - 1:
            error_count = error_count + 1

    print error_count / float(test_num)



def cal_doc_num_of_word(train):
    word = np.ones((61188, 1))
    doc_num = np.unique(train[:, 0]).shape[0]
    doc_num = float(doc_num) + 61188.0

    for i in range(train[:,1].shape[0]):
        index = train[i, 1]
        word[index-1] = word[index-1] + 1

    return np.log(np.divide(doc_num, word + 1))









if __name__ == '__main__':
    # Load training data
    data_dir = 'C:\\Users\\bisai\\Documents\\GitHub\\CSE250B\\data\\20news-bydate\\matlab\\'
    print 'Load training data...'
    train = np.loadtxt('%strain.data'%data_dir, 'int')
    print 'Load training label...'
    train_label = np.loadtxt('%strain.label'%data_dir, 'int')

    total = train_label.shape[0]
    # perm = np.random.permutation(train_num)
    perm = np.load('%sperm.npy'%data_dir)


    train_num = int(0.8 * total)
    # np.save('%sperm'%data_dir, perm)




    train_index = np.in1d(train[:, 0] - 1, perm[0:train_num])
    valid_index = np.in1d(train[:, 0] - 1, perm[train_num:])


    print 'cal weight...'
    word_weight = cal_doc_num_of_word(train[train_index, :])

    print 'finish...'
    # word_weight = cal_doc_num_of_word(train[train_index, :])
    pij = calculate_pi_j(train[train_index, :], train_label)
    pjw = calculate_pj_w(train[train_index, :], train_label)

    word_freq = np.sum(pjw, 1)
    sort_index = np.argsort(word_freq)
    stop_word_index = sort_index[-400:]
    pjw[:, stop_word_index] = 0


    print 'Load test data...'
    test_data = np.loadtxt('%stest.data'%data_dir, 'int')
    print 'Load test label...'
    test_label = np.loadtxt('%stest.label'%data_dir, 'int')

    test(train[valid_index, :], train_label, pij, pjw, word_weight)

    pij = calculate_pi_j(train, train_label)
    pjw = calculate_pj_w(train, train_label)

    # pjw[:, stop_word_index] = 0
    word_weight = cal_doc_num_of_word(train)
    test(test_data,test_label,pij, pjw, word_weight)
