import numpy as np
import matplotlib.pyplot as plt

# Generate some data points for the functions
x = np.linspace(1, 50, 10000)
y1 = 103435 + 4834050/x
y2 = 122480 + 2167802/x

# Plot the functions
plt.plot(x, y1, label='Function 1: x^2')
plt.plot(x, y2, label='Function 2: x^3')

# Add a legend
plt.legend()

# Add labels and title to the plot
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Display the plot
plt.show()
