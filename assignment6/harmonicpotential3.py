N = int(raw_input("Please enter an integer: "))

# System parameters

e = 10.0          # value of epsilon
k = 1100.0        # Spring constant for an H2 molecule
rm = 2.0          # Given in question
m = 2.01588       # For H2, in amu
dt = 0.001        # Time step for each iteration

# Now define initial conditions for t, r, v, and a.

r = 2.
a = 0.
t = 0.
v = 0.

# Here, we'll use an if..elseif (or elif).. else loop to cycle between the temperatures of the system.

for i in range(10000):

# For T = 1000 K

    if T == 1000.0:
        F = N*e*(((rm/r)**12) - 2*((rm/r)**6))
        a = F/m 
        v = ((k*T)/m)**0.5
        r = (r + v*dt)/t
        t = i*dt
        PE = 0.5*k*(r-r0)**2
    
        print t, r, v, PE, F

# Now for T = 2000 K

    elif T==2000.0:
        F = N*e*(((rm/r)**12) - 2*((rm/r)**6))
        a = F/m 
        v = ((k*T)/m)**0.5
        r = (r + v*dt)/t
        t = i*dt
        PE = 0.5*k*(r-r0)**2
    
        print t, r, v, PE, F

# Now for T = 3000 K

    elif T==3000.0:
        F = N*e*(((rm/r)**12) - 2*((rm/r)**6))
        a = F/m 
        v = ((k*T)/m)**0.5
        r = (r + v*dt)/t
        t = i*dt
        PE = 0.5*k*(r-r0)**2
    
        print t, r, v, PE, F

# Now for T = 5000 K

    else T==5000.0:
        F = N*e*(((rm/r)**12) - 2*((rm/r)**6))
        a = F/m 
        v = ((k*T)/m)**0.5
        r = (r + v*dt)/t
        t = i*dt
        PE = 0.5*k*(r-r0)**2
    
        print t, r, v, PE, F



# To plot this, we can use the code from last time as well:

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

t, x1, x2, v1, v2 = loadtxt ('Harmonic Potential - Part 3 (N particle Chain).dat', unpack = True)

figure (1, figsize = (5, 5))

xlabel ('t')
grid(True)
hold(True)
lw = 1

plot (t, x1, 'r', linewidth=lw)
plot (t, x2, 'g', linewidth=lw)

title('Harmonic Potential of a N Particle Chain. )')
savefig('Chain_Harmonic_Potential.png', dpi = 200)

#########Commment############

# As with the previous two cases, we increase the temperature of the dimer's system, and so 
#    the total energy also increases. This in turn forces the internuclear seperation (r) to 
#    increase. So what we observe with increasing T is the separation of the bond lengths 
#    increasing.

# Increasing the temperature of a chain of particles changes the harmonic potential, and thus 
#    chain changes in length also. This is because changing the interaction potential for harmonic 
#    potential results in the average crystal chain length increasing as temperature increases.
#    In particular, the anharmonic potential increases with the temperature. 

# At low temperatures, the N particle chain has the particles' electrons in the ground state.
#    But by increasing the temperature, the ground state electrons are promoted to excited states,
#    resulting in the distance between two adjacent particles increasing. In turn the length of
#    the chain also increases. If observed closely, a macroscopic change in the length of the
#    crystal and the materials' substructure noticeably changes
