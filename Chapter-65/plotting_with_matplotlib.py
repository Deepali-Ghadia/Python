import numpy as np
import matplotlib.pyplot as plt

# simple plot in matplotlib
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, marker = "+")
plt.show()


# using subplots => With the subplot() function you can draw multiple plots in one figure
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1) # three arguments that describes the layout of the figure: rows, colums, position
# two plots will be displayed in single row, i.e. side by side and this is the first plot
plt.plot(x,y, marker = '*', ms=30, mec = 'r', mfc = 'y') # edge color to red | face color to yellow
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph")


#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y, marker = 'o', ms = 10)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph")

plt.suptitle("Using Matplotlib")

plt.show()









