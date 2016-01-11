from MINSTLoader import *
import numpy as np
import scipy as sp
import scipy.spatial as ss
import scipy.io as si

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

    # print 'Build kd-tree...'
    # kd_tree = ss.cKDTree(train_imgs)
    # print 'Testing...'
    # for i in range(0, test_num):
    #     temp, index = kd_tree.query(test_imgs[i,:])
    #     if test_labels[i] != train_labels[index]:
    #         count = count + 1
    # print 'Error %f', count / test_num




if __name__ == '__main__':
    data_dir = '../../data'
    loader = MNIST(data_dir + '/')
    print 'Load training...'
    train_imgs, train_labels = loader.load_training()
    print 'Load testing...'
    test_imgs, test_labels = loader.load_testing()
    # si.savemat('%s/train.mat'%data_dir, {'train':train_imgs, 'tr_l':train_labels})
    # si.savemat('%s/test.mat'%data_dir, {'test':test_imgs, 't_l':test_labels})
    print test_imgs.shape
    print train_imgs.shape
    train_num = train_imgs.shape[0]
    repeat = 20
    error = np.zeros((repeat, 1))
    select = 1000
    OneKNN(train_imgs, train_imgs, test_imgs, test_labels)
    for i in range(0, repeat):
        print 'Test %d...'%i
        ids = np.random.random_integers(0, train_num-1, (1,1000))
        ids = np.squeeze(ids)
        # print ids.shape
        select_train_imgs = train_imgs[ids, :]
        select_train_labels = train_imgs[ids]
        error[i] = OneKNN(select_train_imgs, select_train_labels, test_imgs, test_labels)
    np.save('%s/%d'%(data_dir, select), error)

