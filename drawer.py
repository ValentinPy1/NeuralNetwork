import matplotlib.pyplot as plt
import numpy as np

# Create a blank canvas
canvas = np.zeros((28, 28))

fig, ax = plt.subplots()
ax.imshow(canvas, cmap='gray')

# Variable to keep track of whether the mouse button is down
button_down = False

def on_press(event):
    global button_down
    button_down = True

def on_release(event):
    global button_down
    button_down = False

def on_move(event):
    global canvas  # Add this line
    if button_down:
        # Get mouse coordinates
        x, y = int(event.xdata), int(event.ydata)
        x_grid, y_grid = np.meshgrid(np.arange(28), np.arange(28))
        dist = np.sqrt((x_grid - x)**2 + (y_grid - y)**2)
        sigma = 1
        kernel = np.exp(-dist**2 / (2 * sigma**2))

        canvas += kernel
        
        # Update the figure
        ax.imshow(canvas, cmap='gray')
        fig.canvas.draw()

# Connect the events to the functions
fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()