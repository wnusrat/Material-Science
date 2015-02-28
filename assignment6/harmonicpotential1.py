
# System parameters

k = 1100.0        # Spring constant for an H2 molecule
r0 = 2.0          # Given in question
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
        F = -k*(r-r0)
        a = F/m 
        v = ((k*T)/m)**0.5
        r = (r + v*dt)/t
        t = i*dt
        PE = 0.5*k*(r-r0)**2
    
        print t, r, v, PE

# Now for T = 2000 K

    elif T==2000.0:
        F = -k*(r-r0)
        a = F/m 
        v = ((k*T)/m)**0.5
        r = (r + v*dt)/t
        t = i*dt
        PE = 0.5*k*(r-r0)**2
    
        print t, r, v, PE

# Now for T = 3000 K

    elif T==3000.0:
        F = -k*(r-r0)
        a = F/m 
        v = ((k*T)/m)**0.5
        r = (r + v*dt)/t
        t = i*dt
        PE = 0.5*k*(r-r0)**2
    
        print t, r, v, PE

# Now for T = 5000 K

    else T==5000.0:
        F = -k*(r-r0)
        a = F/m 
        v = ((k*T)/m)**0.5
        r = (r + v*dt)/t
        t = i*dt
        PE = 0.5*k*(r-r0)**2
    
        print t, r, v, PE



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

t, x1, x2, v1, v2 = loadtxt ('Harmonic Potential - Part 1.dat', unpack = True)

figure (1, figsize = (5, 5))

xlabel ('t')
grid(True)
hold(True)
lw = 1

plot (t, x1, 'r', linewidth=lw)
plot (t, x2, 'g', linewidth=lw)

title('Harmonic Potential of an H2 molecule. )')
savefig('H2_Harmonic_Potential_A.png', dpi = 200)

#########Commment############

# As we observed assignment 5, the harmonic potential gives us the 
#    driving force acting on diatomic hydrogen. We can then calculate the potential
#    energy of the system, as well as the usual values of r, t, and v


# As we increase the temperature of the harmonic oscillator's system, then the total energy also 
#    increases. This in turn forces the internuclear seperation (r) to increase. So what we
#    observe with increasing T is the separation of the bond lengths increasing.
#    The energy levels also increase by (h/2pi)*omega for each increase of 1000 K in temperature.

# It is not reasonable to speak about the temperature of an invididual molecule for the harmonic 
#    potential, since the harmonic potential models the change in the distance between two 
#    unattached particles/atoms. The morse potential would more accurately describe the temperature
#    and its relation to the bond distances of an individual molecule.
