import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create some data
x_data = np.linspace(0, 2 * np.pi, 100)
y_data = np.sin(x_data)

# Create a figure and axis
fig, ax = plt.subplots()

# Create an empty line object
line, = ax.plot([], [])

# Function to initialize the plot
def init():
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1, 1)
    return line,

# Function to update the plot for each frame of the animation
def update(frame):
    line.set_data(x_data[:frame], y_data[:frame])  # Update line with data up to current frame
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(x_data), init_func=init, blit=True)

# Display the animation
plt.show()
