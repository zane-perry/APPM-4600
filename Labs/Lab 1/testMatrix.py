import numpy as np
import numpy.linalg as la
import math

def driver():

    m = 2
    n = 2

    #initializing the vector and Matrix that will be used for the program
    A = np.array([[1,2],[3,4]])
    x = np.array([5,6])

    #Calling the helper function
    product = matrixByVector(A,x,m,n)

    print('the product is ', product)

    realProduct = np.matmul(A,x)

    print('the real product is supposed to be', realProduct)

    return
    




def matrixByVector(A,x,m,n):

    result = np.zeros(m)
    
    for i in range(m):
        #Calling dotProduct helper function
        result[i] = dotProduct(A[i],x,n)
        #for every row in A, compute the dot product of that row and the vector x

    return result





def dotProduct(x,y,n):

    #Dot product code taken from the other file
    dp = 0.
    for j in range(n):
       dp = dp + x[j]*y[j]

    return dp


#Final call to the wrapper function to run the entire code
driver()