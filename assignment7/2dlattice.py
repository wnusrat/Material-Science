import numpy as np

na1 = 10
na2 = 10

a1 = np.array([1.,0.,0.]) 
a2 = np.array([0.,1.,0.])

outputFile = open('2Dlattice.xyz', 'w')

outputFile.write (str(na1*na2) + '\n') # a string will give the number of atoms
outputFile.write ('\n')



for n1 in range(na1):  #0, 1, 2 0, 1, 2 for n2
    for n2 in range(na2): # 0, 1, 2 for n2
        R = n1*a1 + n2*a2     
        # print R
        outputFile.write('X ' + ' ' + str(R[0]) +  ' ' + str(R[1]) + ' ' + str(R[2]) + '\n')

outputFile.close( )


#########Commment############
# This is the same as assignment 1, except the lattice is only modelled for 2 dimensions (x and y),
#    and we observe the lattice with the basis given from Figure 8.5 in the textbook.
