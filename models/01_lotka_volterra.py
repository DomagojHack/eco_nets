import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the differential equations
def predator_prey(state, t):
    x, y = state
    dxdt = a*x - b*x*y
    dydt = -c*y + d*x*y
    return dxdt, dydt

# Define the initial conditions
x0 = 10
y0 = 5
state0 = [x0, y0]

# Define the time points for the solution
t = np.linspace(0, 20, 1000)

# Define the model parameters
a = 1.0 # growth rate of the prey population
b = 0.3 # prey mortality due predation
c = 1.0 # growth rate of the predator population (moratility)
d = 0.1 # Predator growth due predation

# Solve the differential equations
states = odeint(predator_prey, state0, t)

# Plot the results
plt.plot(t, states[:, 0], 'r', label='Prey')
plt.plot(t, states[:, 1], 'g', label='Predator')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Population')
plt.show()