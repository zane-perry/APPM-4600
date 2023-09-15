import numpy as np



def driver():

    t = np.linspace(0, np.pi, 31)

    y = np.cos(t)

    sum = 0

    for i in range(31):
        sum += t[i] * y[i]


    print("The sum is: ", sum)


driver()