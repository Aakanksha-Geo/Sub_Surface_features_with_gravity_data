import numpy as np
import matplotlib.pyplot as plt


ro = 0.4*10**3
G_c = 6.67*10**(-11)

filename = 'gravity_values.txt'


def matrix_Gd_file(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
        g = []
        X = []
        for line in lines:
            data = line.split()
            X.append(float(data[0]))
            g.append(float(data[1])*0.01*0.001) # to convert mili gal (mili cm/s^2) to m/s^2 multiply by 0.01*0.001

    # print(g,X)

    G = np.zeros((len(X),4), dtype = "float")
    d = np.zeros(len(X))
    for i in range(len(X)):
        gi = g[i]
        G[i,0] = gi**2
        G[i,1] = 3*gi**2*X[i]**2
        G[i,2] = 3*gi**2*X[i]**4
        G[i,3] = -1
        d[i] = -1*gi**2*X[i]**6
    return G, d




G,d = matrix_Gd_file(filename)
# print(G,d)
GTG = np.dot(np.transpose(G),G)
GTd = np.dot(np.transpose(G),d)

m = np.dot(np.linalg.inv(GTG),GTd)
# print(m)

Z = (m[0]**(1/6) + m[1]**(1/4) + m[2]**(1/2))/3
k = np.sqrt(m[3])/Z
R = ((3*k)/(4*np.pi*G_c*ro))**(1/3)

print(R,Z)



# with open('output.txt','w') as f:
#     i=0
#     for ms in m:
#         f.write('%f \t %d \n'%(ms,i))
#         i+=1
