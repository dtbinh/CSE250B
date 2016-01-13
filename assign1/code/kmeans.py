from MINSTLoader import *
import numpy as np
import scipy as sp
import scipy.spatial as ss
import scipy.io as si
import scipy.stats

def OneKNN(train_imgs, train_labels, test_imgs, test_labels):
    test_num = test_imgs.shape[0]
    count = 0
    dist = []
    # for i in range(0, test_num):
    print 'cal distance'
    dist = ss.distance.cdist(test_imgs, train_imgs, 'euclidean')
    print 'save dist'
    np.save('../../data/dist', dist)
    for i in range(0, test_num):
        index = np.argmin(dist[i, :])
        if test_labels[i] != train_labels[index]:
            count = count + 1
    print count
    error = count / float(test_num)
    print 'Error %f' %error
    return error

def KNNTest(dist, sample_num, test_labels, train_labels):
    train_num = dist.shape[1]
    test_num = dist.shape[0]
    ids = np.random.random_integers(0, train_num-1, sample_num)
    select_dist = dist[:, ids]
    count = 0
    # for i in range(0, test_num):
    #     index = np.argmin(select_dist[i, :])
    #     if test_labels[i] != train_labels[ids[index]]:
    #         count = count + 1
    index = np.argmin(select_dist, axis=1)
    # result = (test_labels != np.array(train_labels[ids[index]]))
    # result = np.equal(test_labels, train_labels[ids[index]])
    # count = len(result.nonzero())

    count = np.count_nonzero(test_labels - train_labels[ids[index]])
    error = count / float(test_num)
    return error

def MeanConfidenceInterval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    return m, h

def UniformSamplingTest(dist, sample_num, test_labels, train_labels, repeat_num):
    error = np.zeros((repeat_num, 1))
    for i in range(0, repeat_num):
        error[i] = KNNTest(dist, sample_num, test_labels, train_labels)
    return error

def PrototypeSelectionTest(sample_num, test_labels, train_labels, repeat_num):



if __name__ == '__main__':
    data_dir = '../../data'
    loader = MNIST(data_dir + '/')
    print 'Load training...'
    train_imgs, train_labels = loader.load_training()
    print 'Load testing...'
    test_imgs, test_labels = loader.load_testing()

    print 'Load dist...'
    dist = np.load('%s/dist.npy'%data_dir)
    sample_num = 10000
    repeat_num = 50
    error = UniformSamplingTest(dist, sample_num, test_labels, train_labels, repeat_num)
    mean_error, interval = MeanConfidenceInterval(error)
    print mean_error
    print interval
    np.save('%s/error_%d'%(data_dir, sample_num), error)
    np.save('%s/result_%d'%(data_dir, sample_num), [mean_error, interval])


