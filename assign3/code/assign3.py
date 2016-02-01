import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

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


if __name__ == "__main__":
    mean = np.array([0,0])
    cov_matrix = np.array([[1,-0.75],[-0.75,1]])
    PlotBivGaussian(mean, cov_matrix)
