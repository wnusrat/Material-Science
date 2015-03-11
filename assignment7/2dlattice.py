import numpy as np

nx = 10
ny = 10

outputFile = open('2Dlattice.xyz', 'w')


x1 = np.array([1.,0.,0.]) 
x2 = np.array([0.,1.,0.])

outputFile.write(str(nx*ny) + ' \n')
outputFile.write(' \n')


for i in range(nx): #0..10 for nx
    for j in range(ny): #0 .. for ny
        R = nx*x1 + ny*x2      # print R
            outputFile.write ('Y ' + str(R[0]) + ' ' + str(R[1]) + ' ' + str(R[2]) + ' \n')

outputFile.close()

#########Commment############
# This is the same as assignment 1, except the lattice is only modelled for 2 dimensions (x and y),
#    and we observe the lattice with the basis given from Figure 8.5 in the textbook.
