# here the goal is to make the orthorhombic crystal, so we need for the third vector to have the values halved
import numpy as np

na1 = 30
na2 = 30
na3 = 30

a1 = np.array([1.,0.,0.]) 
a2 = np.array([0.,1.,0.])
a3 = np.array([0.5,0.5,0.5])

# a1 = np.array([0.5, 0.5, 0.0]) 
# a2 = np.array([0.5, 0.0, 0.5])
# a3 = np.array([0.0, 0.5, 0.5])

outputFile = open('primative mono.xyz', 'w')

outputFile.write (str(na1*na2*na3) + '\n')
outputFile.write ('\n')



for n1 in range(na1):  #0, 1, 2 0, 1, 2 for n2
    for n2 in range(na2): # 0, 1, 2 for n2
        for n3 in range(na3): #0, 1, 2 for n3
            R = n1*a1 + n2*a2 + n3*a3      
            # print R
            outputFile.write('X ' + ' ' + str(R[0]) +  ' ' + str(R[1]) + ' ' + str(R[2]) + '\n')


outputFile.close( )
            # Instead of just printing to the screen, we will make xyz file to visualize the lattices

# loop allows you to cycle through all the numbers in each space of vector
 
# removing just the print function gives the R as a vector
