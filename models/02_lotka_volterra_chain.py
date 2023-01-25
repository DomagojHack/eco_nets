import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the function for the differential equations
def lotka_volterra( t, init, alpha, beta, gamma, delta, epsilon, mu):
    x = init[0]
    y = init[1]
    z = init[2]
    dxdt = alpha*x - beta*x*y
    dydt = -gamma*y + delta*x*y - epsilon*y*z
    dzdt = mu*y*z - z
    return [dxdt, dydt, dzdt]

# Set the parameter values
alpha = 1.0
beta = 0.1
gamma = 1.5
delta = 0.75
epsilon = 0.5
mu = 0.1

# Initial conditions
x0 = 10
y0 = 5
z0 = 2

init = [x0, y0, z0]

# Time points for the solution
t = np.linspace(0, 15, 1000)

# Solve the differential equations
sol = solve_ivp(lotka_volterra, (0, 15), init, args=(alpha, beta, gamma, delta, epsilon, mu), t_eval=t)

# Plot the solution
plt.plot(sol.t, sol.y[0], label='Prey 1')
plt.plot(sol.t, sol.y[1], label='Predator 1')
plt.plot(sol.t, sol.y[2], label='Predator 2')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.show()
