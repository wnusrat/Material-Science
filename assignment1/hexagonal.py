#I wasn't sure about this one. I read that there should be two basis vectors, but how would I implement that in
# this code. Should there the vectors (b1 and b2) present?
import numpy as np

na1 = 3
na2 = 3
na3 = 3
#nb1 = 30
#nb2 = 30

a1 = np.array([1.0, 0.0, 0.0]) 
a2 = np.array([0.5, 0.87, 0.0])
a3 = np.array([0.0,0.0,1.0])
#b1 = np.array([0.0,0.0,0.0])
#b2 = np.array([.33,.33,0.5])

#b1 and b2 for basis vectors of (0,0,0) and (1/3, 1/3, 1/2)

#a1 = np.array([1.0, .0, .0])
#a2 = np.array([.0, 1.0, .0])
#a3 = np.array([0.5, 0.5, 0.5])

outputFile = open('hexagonal.xyz', 'w')

outputFile.write (str(na1*na2*na3) + '\n')
outputFile.write ('\n')



for n1 in range(na1):  #0, 1, 2 0, 1, 2 for n2
    for n2 in range(na2): # 0, 1, 2 for n2
        for n3 in range(na3): #0, 1, 2 for n3
            R = n1*a1 + n2*a2 + n3*a3   
            # print R
            outputFile.write('X ' + ' ' + str(R[0]) +  ' ' + str(R[1]) + ' ' + str(R[2]) + '\n')


outputFile.close()

# Instead of just printing to the screen, we will make xyz file to visualize the lattices

# loop allows you to cycle through all the numbers in each space of vector
# removing just the print function gives the R as a vector
