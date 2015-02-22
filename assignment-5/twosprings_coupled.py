

# System parameters

# First the masses
m1 = 3.0
m2 = 3.0

# Then the spring constants (both are equal, so use k):

k = 20.0

# Lengths of the springs (assume equal to one)

L1 = 1.0
L2 = 1.0

# Now the initial conditions. 
#     x1 and x2 are the initial displacements
#     v1 and v2 are the initial velocities


x1 = 4.0
x2 = 6.0

v1 = 0.0
v2 = 0.0

# We'll use a time step of 0.001 s like in question 3

dt = 0.001

# Now define initial conditions for acceleration and time

v = 0.
a = 0.
t = 0.

# Use F1, a1, v1, and t for mass 1
# Use F2, a2, v2, and t for mass 2

for i in range(10000):
    
    F1 = -k*x1 + k*(x2-x1)
    F2 = -k*(x2-x1) + k*(-x2)
    a1 = F1/m1
    a2 = F2/m2 
    
    v1 = v1 + a1*dt
    x1 = x1 + v1*dt
    

    v2 = v2 + a2*dt
    x2 = x2 + v2*dt
    
    t = i*dt
    

    
    print t, x1, v1, a1, F1
    print t, x2, v2, a2, F2
    # get particle to start at eq'm position and stay at same position


# Now for the plot, we need parameters

absolute_err = 1.0e-8
relative_err = 1.0e-6
stopping_time = 10.0
number_points = 250.0

# Lets set up the number of points for the output.
# A number of 250 points will give a better graph (more points).

t_stop = [stopping_time * float(i) / (number_points - 1) for i in range(number_points)]

# Now we can plot the solution

from numpy import loadtxt
from pylab import figure, plot, xlabel, grid, hold, legend, title, savefig

from matplotlib.font_manager import FontProperties

t, x1, x2, v1, v2 = loadtxt ('twospring_coupled.dat', unpack = True)

figure (1, figsize = (5, 5))

xlabel ('t')
grid(True)
hold(True)
lw = 1

plot (t, x1, 'r', linewidth=lw)
plot (t, x2, 'g', linewidth=lw)

title('Displacement of 2 Coupled-Mass Spring Systems')
savefig('Coupled_Springs.png', dpi = 200)


#########Commment############


# We first observe that the elastic force gives us a total driving 
#   force acting on each mass. Though they have the same mass, they 
#   have different positions, so they therefore have 2 accelerations, 
#   and thus two different potential energies and forces.



# In some instances, we may observe the springs going into each other.



