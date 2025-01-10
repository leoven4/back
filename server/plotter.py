import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

# Initialize the plot
fig, ax = plt.subplots()
x_data, y_data = [], []

# Set the limits for the plot (adjust as necessary)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)



# Plotting function to update the graph
def update_plot(frame):

    
    data = pd.read_csv('server/x.txt', sep=" ", header=None)
    data.columns = ["x"]
    
    # Limit the length of the data to the last 100 points

    x_data = data.x[-100:-1]
    # Clear the previous plot and re-plot the updated data
    ax.clear()
    ax.plot(data.x)
    ax.set_xlim(len(data.x)-100, len(data.x))
    ax.set_ylim([min(x_data) - 0.02, max(x_data) + abs(max(x_data))+0.02])  # Adjust the y-axis dynamically

ani = FuncAnimation(fig, update_plot, frames=range(1000), interval=100)
ax.autoscale(axis='y')  # Autoscale only the y-axis
plt.show()
