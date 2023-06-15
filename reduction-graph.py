import numpy as np
import matplotlib.pyplot as plt
# Print data

# Generate some data points for the functions
x = np.linspace(1, 100, 10000)
y1 = (1 - (122480*x + 2167802) / (183315*x + 4834050)) * 100


# Plot the functions
plt.plot(x, y1, label='Gas cost reduction rate of the proposed methodology, comparing to succinctly verifiable sealed bid auction')

# Add a legend
plt.legend()

# Add labels and title to the plot
plt.xlabel('Number of bidders')
plt.ylabel('Reduction rate (%)')

# Display the plot
plt.show()

