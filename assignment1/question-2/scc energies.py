# We first start with the simple cubic

import numpy as np
# from numpy import *

a1 = np.array([1.,0.,0.]) 
a2 = np.array([0.,1.,0.])
#a3 = np.array([0.,0.,1.])


# outputFile = open('scc energies.xyz', 'w')

#outputFile.write (str(na1*na2*na3) + '\n') # a string will give the number of atoms
#outputFile.write ('\n')

#define all other variables
r_m = 2 
e = 10
natom = 10


r = n2*a2 - n1*a1 # 
nsteps = int(r*natom) #number of steps

#empty arrays to hold values
natom = 20
#natom2 = np.empty(nsteps)

#set initial values (i.c's)
n1[0] = 0
n2[0] = 0

for i in range (0, natom + 1):
    for j in range (0, natom + 1):
        r[i + 1] = n2[i]*a2 - n1[i]*a1
        V[i + 1] = e*( (r_m/r[i + 1]**12 - 2(r_m/r[i + 1])**6 )
        Vtotal[i + 1] = V[i + 1]/2

print Vtotal[i + 1]/2

#outputFile.write('V ' + ' ' + str(Vtot[0]) +  ' ' + str(Vtot[1]) + ' ' + str(Vtot[2]) + '\n')





# this is just from previous scc code (ignore)
#for n1 in range(na1):  #0, 1, 2 0, 1, 2 for n2
 #   for n2 in range(na2): # 0, 1, 2 for n2
  #      for n3 in range(na3): #0, 1, 2 for n3
   #         R = n1*a1 + n2*a2 + n3*a3      
    #        # print R
     #       outputFile.write('X ' + ' ' + str(R[0]) +  ' ' + str(R[1]) + ' ' + str(R[2]) + '\n')


#outputFile.close( )
# Instead of just printing to the screen, we will make xyz file to visualize the lattices
# loop allows you to cycle through all the numbers in each space of vector
# removing just the print function gives the R as a vector
