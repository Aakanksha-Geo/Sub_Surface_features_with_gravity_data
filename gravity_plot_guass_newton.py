import numpy as np
import matplotlib.pyplot as plt

R0 = 200.0
ro = 0.4*10**3
G = 6.67*10**(-11)
Z0 = 500.0
iterations = 5

def f(x, R, Z):
    g = (4*np.pi*G*ro*Z*R**3)/(3*(x**2 + Z**2)**(3.0/2.0))
    return g

def dg_dR(x, R, Z):
    ans = (4*np.pi*G*ro*Z*R**2)/((x**2 + Z**2)**(3.0/2.0))
    return ans

def dg_dZ(x, R, Z):
    ans = (4*np.pi*G*ro*R**3)*(x**2 - 2*Z**2)/(3*(x**2 + Z**2)**(5.0/2.0))
    return ans

def matrix_A(X, R, Z):
    A = np.zeros((len(X),2), dtype = "float")
    for i in range(len(X)):
        A[i,0] = dg_dR(X[i], R, Z)
        A[i,1] = dg_dZ(X[i], R, Z)
    return A

def matrix_y(X,R0,Z0,R,Z):
    y = np.zeros(len(X))
    for i in range(len(X)):
        y[i] = f(X[i], R0, Z0) - f(X[i], R, Z)
    return y

X = np.linspace(-1200, 1200, 100)
R1 = float(input("Enter initial guess for R "))
Z1 = float(input("Enter initial guess for Z "))

# R = 190
# Z = 490
R=R1
Z=Z1
iter = []
error = []
for i in range(iterations):
    A = matrix_A(X, R, Z)
    y = matrix_y(X, R0, Z0, R, Z)
    ATA = np.dot(np.transpose(A),A)
    ATY = np.dot(np.transpose(A),y)
    # print(np.linalg.inv(ATA).shape)
    del_m = np.dot(np.linalg.inv(ATA),ATY)
    err = np.sqrt(np.sum(np.dot(y,y))/len(X))
    error.append(err)
    iter.append(i+1)
    R = R + del_m[0]
    Z = Z + del_m[1]
    print(del_m, R, Z)

# print(error)
with open('Gradient_output.txt','a') as f:
    f.write('%f \t %f \t %f \t %f \n'%(R1,Z1,R,Z))




plt.plot(iter,error, "-o", lw = 2)
plt.xlabel("Itertion Number",fontsize=16)
plt.ylabel("Error",fontsize=16)
plt.text(2, error[0]-0.1*error[0], "Inital Guess R = {}, Z = {}".format(R1,Z1), fontsize=12)
plt.text(2, error[0]-0.2*error[0], "Actual Value R = {}, Z = {}".format(R0,Z0), fontsize=12)

plt.savefig('Gravity_guass_newton_{}_{}.png'.format(int(R1),int(Z1)),format='png',dpi=350)
plt.show()
