from MINSTLoader import *
import numpy as np
import scipy as sp
import scipy.spatial as ss
import scipy.io as si
import scipy.stats
import scipy.cluster as sc
import sklearn.cluster as sklearn

def AnotherTest(train_imgs, train_labels, test_imgs, test_labels):
    


def OneKNN(train_imgs, train_labels, test_imgs, test_labels):
    test_num = test_imgs.shape[0]
    print 'cal distance'
    dist = ss.distance.cdist(test_imgs, train_imgs, 'euclidean')
    print test_labels.shape
    index = np.argmin(dist, axis=1)

    labels = np.squeeze(train_labels[index])
    print labels.shape
    count = np.count_nonzero(test_labels - labels)
    error = count / float(test_num)

    # error = count / float(test_num)
    print 'Error %f' %error
    # return error
    return error

def KNNTest(dist, sample_num, test_labels, train_labels):
    train_num = dist.shape[1]
    test_num = dist.shape[0]
    ids = np.random.random_integers(0, train_num-1, sample_num)
    select_dist = dist[:, ids]

    index = np.argmin(select_dist, axis=1)
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

def PrototypeSelectionTest(sample_num, train_imgs, train_labels, test_imgs, test_labels, repeat_num):
    error = np.zeros((repeat_num, 1))
    cluster = sklearn.MiniBatchKMeans(sample_num, 'k-means++', 100, sample_num)
    for i in range(0, repeat_num):
        print 'kmeans...'
        # centroid, label = sc.vq.kmeans2(train_imgs, sample_num, iter=50)
        cluster.fit_predict(train_imgs)
        centroid = cluster.cluster_centers_
        label = cluster.labels_
        print centroid.shape
        print label.shape
        print 'kmeans finsihed...'
        centroid_label = np.zeros((sample_num, 1))
        for j in range(0, sample_num):
            idx = np.where(label == j)
            most_label = train_labels[idx]
            centroid_label[j] = scipy.stats.mode(most_label)[0][0]
        error[i] = OneKNN(centroid, centroid_label, test_imgs, test_labels)
    return error





if __name__ == '__main__':
    data_dir = '../../data'
    loader = MNIST(data_dir + '/')
    print 'Load training...'
    train_imgs, train_labels = loader.load_training()
    print 'Load testing...'
    test_imgs, test_labels = loader.load_testing()

    print test_labels.shape
    # print 'Load dist...'
    # dist = np.load('%s/dist.npy'%data_dir)
    sample_num = 5000
    repeat_num = 1
    # error = UniformSamplingTest(dist, sample_num, test_labels, train_labels, repeat_num)
    # mean_error, interval = MeanConfidenceInterval(error)
    error = PrototypeSelectionTest(sample_num, train_imgs, train_labels, test_imgs, test_labels, repeat_num)
    print error
    mean_error, interval = MeanConfidenceInterval(error)
    print mean_error
    print interval
    np.save('%s/pro_error_%d'%(data_dir, sample_num), error)
    np.save('%s/pro_result_%d'%(data_dir, sample_num), [mean_error, interval])


