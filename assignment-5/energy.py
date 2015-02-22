

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
    KE = 0.5*m*v**2
    PE = 0.5*k*(x-x0)**2
    E_total = KE + PE

    print t, KE, PE, E_total

    # get particle to start at eq'm position and stay at same position

