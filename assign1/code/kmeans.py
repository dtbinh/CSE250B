from MINSTLoader import *
import numpy as np
import scipy as sp
import scipy.spatial as ss

def OneKNN(train_imgs, train_labels, test_imgs, test_labels):
    test_num = len(test_imgs)
    count = 1
    # for i in range(0, test_num):
    # dist = ss.distance.cdist(test_imgs, train_imgs, 'euclidean')
    # for i in range(0, test_num):
    #     index = np.argmax(dist[i, :])
    #     if test_labels[i] != train_labels[index]:
    #         count = count + 1
    # print 'Error %f', count / test_num
    kd_tree = ss.cKDTree(train_imgs)
    for i in range(0, test_num):
        temp, index = kd_tree.query(test_imgs[i,:])
        if test_labels[i] != train_labels[index]:
            count = count + 1
    print 'Error %f', count / test_num




if __name__ == '__main__':
    loader = MNIST('../../data/')
    train_imgs, train_labels = loader.load_training()
    test_imgs, test_labels = loader.load_testing()
    print test_imgs.shape
    print train_imgs.shape

    OneKNN(train_imgs, train_labels, test_imgs, test_labels)

