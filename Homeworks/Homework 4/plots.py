import scipy
import numpy as np
import matplotlib.pyplot as plt

def driver():

    #x = np.linspace(0, 1, 500)
    #Ts = -15
    #Ti = 20
    #alpha = 0.138e-6
    #t = 60 * 60 * 24 * 60
    #f = lambda x: ((Ti - Ts) * scipy.special.erf(x / (2 * np.sqrt(alpha * t)))) + Ts
    #y = f(x)


    #plt.plot(x,y)
    #plt.hlines(0, 0, 1, color='r', linestyles='--')
    #plt.xlabel("x")
    #plt.ylabel("y")
    #plt.title("f(x)")
    #plt.show()

    x1 = np.array([0.8652758615984806, 0.5459041338497894,0.2960148498375430,0.1202468177079170,0.0268142943717937,0.0016291357689859,0.0000063899421097,0.0000000000987017])
    y1 = np.array([0.5459041338497894,0.2960148498375430,0.1202468177079170,0.0268142943717937,0.0016291357689859,0.0000063899421097,0.0000000000987017, 0])

    x2 = np.array([0.1347241384015194,0.1185951061434549,0.0558536302751180,0.0170683074599678,0.0021925881853864,0.0000926696033334,0.0000004924528145,0.0000000001103035])
    y2 = np.array([0.1185951061434549,0.0558536302751180,0.0170683074599678,0.0021925881853864,0.0000926696033334,0.0000004924528145,0.0000000001103035, 0])

    plt.loglog(x1,y1)
    plt.loglog(x2,y2)
    plt.legend(['Newton\'s Method', 'Secant Method'])
    plt.xlabel("|x(n) - r|")
    plt.ylabel("|x(n+1) - r|")
    plt.title("Errors of Newton's and secant methods")
    plt.show()

driver()