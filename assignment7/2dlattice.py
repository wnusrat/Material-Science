dx = 1.0
dy = 1.0

nx = 10
ny = 10

outputFile = open('2Dlattice.xyz', 'w')

outputFile.write(str(nx*ny) + ' \n')
outputFile.write(' \n')

for i in range(nx):
    for j in range(ny):
            outputFile.write ('Y ' + str(i*dx) + ' ' + str(j*dy) + ' ' + ' \n')

outputFile.close()



#########Commment############

# This is the same as assignment 1, except the lattice is only modelled for 2 dimensions (x and y),
#    and we observe the lattice with the basis given from Figure 8.5 in the textbook.
