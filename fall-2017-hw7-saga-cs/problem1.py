import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

def power_iteration(A, tolerance):
    """ Solve for the largest eigenvalue of a matrix using the power iteration method
        Arguments:
        A -- is the matrix
        tolerance -- a measure of accuracy of the result       
        Returns a tuple of (k,x,count) as defined:
        The final estimate of the largest eigenvalue, k.
        The final estimate of the corresponding eigenvector, x.
        The number of iterations that it took to reach convergence, count."""

    x = np.ones((A.shape[0]))
    res_inf_norm = tolerance + 5
    count = 0
    while res_inf_norm > tolerance:
        count+=1
        y = np.dot(A, x)
        k = np.linalg.norm(y)
        x = y / k
        residual = np.dot(A,x) - k*x
        res_inf_norm = np.linalg.norm(residual)

    return (k,x,count)

def main():
    np.random.seed(1)
    A = np.random.rand(5, 5)
    x = [math.pow(10,-3), math.pow(10,-4), math.pow(10,-5), math.pow(10,-6), math.pow(10,-7), math.pow(10,-8)]
    print(power_iteration(A, math.pow(10,-3)))
    print(np.linalg.eigvals(A))
    y = []
    for i in x :
        y.append(power_iteration(A, i)[2])
    plt.semilogx(x,y)
    plt.xlabel('Tolerance Used') 
    plt.ylabel('Number of Iterations')
    plt.show()
    plt.savefig("iterations.png")

if __name__ == '__main__':
    main()