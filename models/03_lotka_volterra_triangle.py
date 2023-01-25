import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the predator-prey model
def lotka_volterra(t, y, a, b, c, d, e, f, g):
    x, y, z = y
    dxdt = a*x - b*x*y - c*x*z # elk population growth rate = elk population x (growth rate - predation rate by wolf - predation rate by bear)
    dydt = d*x*y - e*y - f*y*z # wolf population growth rate = wolf population x (predation rate of elk - death rate - predation rate of bear)
    dzdt = g*y*z - b*z # bear population growth rate = bear population x (predation rate of wolf - death rate)
    return [dxdt, dydt, dzdt]

# Initial conditions
x0 = 100 #initial elk population
y0 = 20 #initial wolf population
z0 = 30 #initial bear population

# Model parameters
a = 0.1 #elk growth rate
b = 0.01 #elk predation rate by wolf
c = 0.01 #elk predation rate by bear
d = 0.05 #wolf predation rate of elk
e = 0.2 #wolf death rate
f = 0.01 #wolf predation rate of bear
g = 0.05 #bear predation rate of wolf

# Time array for the solution
t = np.linspace(0, 50, 1000)

# Solve the ODE using the scipy.integrate.solve_ivp function
solution = solve_ivp(lotka_volterra, [0, 50], [x0, y0, z0], args=(a, b, c, d, e, f, g), t_eval=t)

# Plot the results
plt.plot(solution.t, solution.y[0], label='Elk')
plt.plot(solution.t, solution.y[1], label='Wolves')
plt.plot(solution.t, solution.y[2], label='Bears')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Population')
plt.show()
