import numpy as np



def driver():

    s = np.pi / 2
    forward = lambda h: ((np.cos(s + h) - np.cos(s)) / h)
    center = lambda h: ((np.cos(s + h) - np.cos(s - h)) / (2*h))

    h = 0.01 * 2.**(-np.arange(0,10))

    forwardDifference = forward(h)
    centeredDifference = center(h)

    print('Forward Difference:')
    for it in range(forwardDifference.size):
         print('%16.16e' % forwardDifference[it])

    print('Centered Difference:')
    for it in range(centeredDifference.size):
         print('%16.16e' % centeredDifference[it])

driver()