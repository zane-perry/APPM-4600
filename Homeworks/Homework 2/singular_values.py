import numpy as np

def driver():

    A = (1/2) * np.array([[1, 1], [1 + (10 ** -10), 1- (10 ** -10)]])

    svd = np.linalg.svd(A)

    v = svd[1]

    k = v[0] / v[1]

    print("The condition number of A is: ",k)


driver()