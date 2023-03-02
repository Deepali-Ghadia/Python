# using seaborn
# Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot([0, 10, 20, 30, 40, 50])
plt.show()

# without histogram
# sns.distplot([0, 10, 20, 30, 40, 50], hist=False)



# using matplotlib
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x,y)
plt.plot(x,y, color='red')
plt.scatter(x,y, color='yellow')
plt.show()


# plotly




# mayaVI