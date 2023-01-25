import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the model
def lotka_volterra(state, t):
    x = state[0] # Plankton population
    y = state[1] # Krill population
    z = state[2] # Whale population
    a = 0.1      # Plankton growth rate
    b = 0.02     # Krill growth rate
    c = 0.001    # Whale growth rate
    d = 0.002    # Plankton death rate
    e = 0.01     # Krill death rate
    f = 0.00005  # Whale death rate
    g = 0.0002   # Plankton loss due to Krill
    h = 0.00005  # Krill loss due to Whale
    i = 0.00005  # Plankton gain due to Whale
    j = 0.0001   # Krill gain due to Whale
    return [a*x - d*x - g*x*y, b*y*x - e*y - h*y*z, c*z*y - f*z - i*z*x + j*z*y]

# Initial conditions
init = [50, 10, 1]

# Time points
t = np.linspace(0, 50, 1000)

# Solve the model
state = odeint(lotka_volterra, init, t)

# Plot the results
plt.figure(figsize=(15,15))
plt.plot(t, state[:, 0], 'g', label='Plankton')
plt.plot(t, state[:, 1], 'b', label='Krill')
plt.plot(t, state[:, 2], 'r', label='Whale')
plt.legend(loc='best')
plt.xlabel('Time')
plt.ylabel('Population')
plt.show()