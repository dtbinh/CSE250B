import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from MINSTLoader import *
import scipy.io as sio

def PlotBivGaussian(mean, cov_matrix):
    samples = np.random.multivariate_normal(mean, cov_matrix, 100)

    fig = plt.figure()
    fig.suptitle('Problem 2-b', fontsize=20, fontweight='bold')
    ax = fig.add_subplot(111)

    x = samples[:, 0]
    y = samples[:, 1]
    ax.scatter(x,y, 40, "#e12727")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    plt.savefig('./2-b.png',dpi=100)
    plt.show()
    return samples

def PlotBoundary():
    x = np.linspace(-10, 4, 500, endpoint=True)
    y = (3 * x + 12) / 4

    fig = plt.figure()
    fig.suptitle('Problem 3', fontsize=20, fontweight='bold')
    ax = fig.add_subplot(111)
    ax.plot(x, y)

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    plt.annotate(r'$(-4,0)$',
             xy=(-4, 0), xycoords='data',
             xytext=(-20, +60), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    plt.annotate(r'$(0,3)$',
             xy=(0, 3), xycoords='data',
             xytext=(+10, -30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    plt.annotate(r'positive',
             xy=(-6, 2), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16)

    # ax.set_xlabel("x")
    # ax.set_ylabel("y")

    plt.savefig('./3.png', dpi = 100)
    plt.show()


def GaussianClassifier():
    data_dir = '../../data'
    loader = MNIST(data_dir + '/')
    print 'Load training...'
    train_imgs, train_labels = loader.load_training()
    print 'Load testing...'
    test_imgs, test_labels = loader.load_testing()
    sio.savemat('../../data/MNIST.mat', {'train_imgs':train_imgs, 'train_labels':train_labels,
                                        'test_imgs':test_imgs, 'test_labels':test_labels})


    # generate a validation dataset










if __name__ == "__main__":

    prob = "4"

    if prob == "2-b":
        mean = np.array([0,0])
        cov_matrix = np.array([[1,-0.75],[-0.75,1]])
        PlotBivGaussian(mean, cov_matrix)
    elif prob == "3":
        PlotBoundary()
    elif prob == "4":
        GaussianClassifier()


