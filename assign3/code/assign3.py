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

def MyPlot(x, y, filename, title, x_label, y_label):

    fig = plt.figure()
    fig.suptitle(title, fontsize=20, fontweight='bold')
    ax = fig.add_subplot(111)
    ax.plot(x, y)

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    # plt.annotate(r'$(-4,0)$',
    #          xy=(-4, 0), xycoords='data',
    #          xytext=(-20, +60), textcoords='offset points', fontsize=16,
    #          arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    #
    # plt.annotate(r'$(0,3)$',
    #          xy=(0, 3), xycoords='data',
    #          xytext=(+10, -30), textcoords='offset points', fontsize=16,
    #          arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    #
    # plt.annotate(r'positive',
    #          xy=(-6, 2), xycoords='data',
    #          xytext=(+10, +30), textcoords='offset points', fontsize=16)
    for index in  [4, 9, 14, 19]:
        plt.annotate('$(' + str(float(x[index])) + ', ' + '{:.2f}'.format(float(y[index])) + ')$',
                 xy=(x[index], y[index]), xycoords='data',
                 xytext=(-60, 40), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    plt.savefig(filename, dpi = 100)
    plt.show()


def GaussianClassifier():
    data = sio.loadmat('../../prob6.mat');
    f  = data.get('f')
    error = data.get('error_rate') * 100
    abstain_fraction = data.get('abstain_fraction')
    final_abstain = data.get('final_abstain')

    # MyPlot(np.transpose(f), error, './6-error.png', r'Error rate on different $f$', 'f', 'error rate')
    MyPlot(np.transpose(f), abstain_fraction, './6-fraction.png', r'Abstain fraction on different $f$', 'f', 'abstain fraction')



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


