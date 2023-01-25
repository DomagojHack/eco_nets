import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the predator-prey equations (5 organisms)
def predator_prey(t, y, a, b, c, d, e, f, g, h, i, j):
    x1, x2, x3, x4, x5 = y
    return [a*x1 - b*x1*x2 - c*x1*x3 - d*x1*x4 - e*x1*x5,
            -f*x2 + g*x1*x2 + h*x3*x2 + i*x4*x2 + j*x5*x2,
            -g*x3 + h*x2*x3 - i*x3*x4 - j*x3*x5,
            -h*x4 + i*x3*x4 - j*x4*x5,
            -i*x5 + j*x3*x5 + j*x4*x5]

# Set initial conditions and parameter values
x0 = [10, 5, 8, 15, 20]
a = 0.1
b = 0.02
c = 0.03
d = 0.04
e = 0.05
f = 0.06
g = 0.07
h = 0.08
i = 0.09
j = 0.1

# Time range for the solution
t_eval = np.linspace(0, 50, 1000)

# Solve the ODE using the solve_ivp function
sol = solve_ivp(predator_prey, [0, 50], x0, args=(a, b, c, d, e, f, g, h, i, j), t_eval=t_eval)

# Plot the solution
plt.plot(sol.t, sol.y[0], label='Organism 1')
plt.plot(sol.t, sol.y[1], label='Organism 2')
plt.plot(sol.t, sol.y[2], label='Organism 3')
plt.plot(sol.t, sol.y[3], label='Organism 4')
plt.plot(sol.t, sol.y[4], label='Organism 5')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.show()