
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

# Define the function
def equation(x):
    return np.sin(x) + (3/4) * x - 1

# Generate x values
x_values = np.linspace(0, 6, 1000)

# Calculate y values
y_values = equation(x_values)

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=r'$\sin(x) + \frac{3}{4}x - 1$', color='blue')
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)  # Add horizontal line at y=0

# Add labels and title
plt.title('Graph of $sin(x) + \\frac{3}{4}x - 1$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
