

# System parameters

k = 20.0
m = 3.0
x0 = 4.
dt = 0.001

# Now define initial conditions

x = 2.
v = 0.
a = 0.
t = 0.


for i in range(10000):
    
    F = -k*(x-x0)
    a = F/m 
    v = v + a*dt
    x = x + v*dt
    t = i*dt
    
    print t, x
    # get particle to start at eq'm position and stay at same position



#########Commment############

# We first observe that the elastic force gives us a total driving force acting on each mass. 
# Though they have the same mass, they have different positions,
# so they therefore have 2 accelerations, and thus two different potential energies and forces.


# We observe a graph for the energies where the kinetic energy and 
#    potential energy oscillate from minimum to maximum as time 
#    increases. This results in two sinusoidal curves, and a solid 
#    horizontal line representing the total energy.

# In some instances, we may observe the springs going into each other.


# If the step size is ten times smaller, then get faster oscillations, but no change in energy.
# If step size is ten time greater, then get slower oscillations, but no change in energy.
