import numpy as np
import matplotlib.pyplot as plt
# Print data
def logOutputs(upperRange):
    for i in range(2,upperRange):
        print(i)
        myValue = 122480 + 2167802/i 
        GalaValue = 183315 + 4834050/i
        print("my: ",myValue)
        print("Galal: ",GalaValue)
        print("%", ( 1- (myValue / GalaValue)) * 100)
        print()
        print("*******")

logOutputs(100)

# Generate some data points for the functions
x = np.linspace(1, 30, 10000)
y1 = 183315 + 4834050/x
y2 = 122480 + 2167802/x


# Plot the functions
plt.plot(x, y1, label='Succinctly Verifiable Sealed-bid Auction')
plt.plot(x, y2, label='Proposed Methodology')

# Add a legend
plt.legend()

# Add labels and title to the plot
plt.xlabel('Number of bidders')
plt.ylabel('Gas cost')

# Display the plot
plt.show()

