##import matplotlib.pyplot as plt
##
###Simple plot
## 
##x = [1,2,3]
##y = [2,4,1]
## 
####plt.plot(x, y)
##
### plotting the points
####plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
####         marker='o', markerfacecolor='blue', markersize=12)
##
##plt.scatter(x, y, label= "stars", color= "red",
##            marker= "*", s=55)
## 
### setting x and y axis range
####plt.ylim(1,8)
####plt.xlim(1,8)
## 
##plt.xlabel('x - axis')
##plt.ylabel('y - axis')
## 
##plt.title('My first graph!')
## 
##plt.show()
##
#######
##
###Plot 2 lines on same graph
##
### line 1 points
##x1 = [1,2,3]
##y1 = [2,4,1]
### plotting the line 1 points
##plt.plot(x1, y1, label = "line 1")
## 
### line 2 points
##x2 = [1,2,3]
##y2 = [4,1,3]
### plotting the line 2 points
##plt.plot(x2, y2, label = "line 2")
##
##plt.xlabel('x - axis')
##plt.ylabel('y - axis')
##
##plt.title('Two lines on same graph!')
## 
##plt.legend()
## 
##plt.show()
##
##
#######
##
###3d graph
##
##from mpl_toolkits.mplot3d import axes3d #this module needed for 3d
##from matplotlib import style
##import numpy as np
## 
### setting a custom style to use
##style.use('ggplot')
## 
### create a new figure for plotting
##fig = plt.figure()
## 
### create a new subplot on our figure
### and set projection as 3d
##ax1 = fig.add_subplot(111, projection='3d')
## 
### defining x, y, z co-ordinates
##x = np.random.randint(0, 10, size = 20)
##y = np.random.randint(0, 10, size = 20)
##z = np.random.randint(0, 10, size = 20)
## 
### plotting the points on subplot
##ax1.plot_wireframe(x,y,z)
## 
### setting labels for the axes
##ax1.set_xlabel('x-axis')
##ax1.set_ylabel('y-axis')
##ax1.set_zlabel('z-axis')
## 
### function to show the plot
##plt.show()
##






import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-25,25,100)

# the function, which is y = x^3 here
y = x**2 + 3*x

# setting the axes at the centre
#fig = plt.figure()
plt.plot(x, y, label = "line 1")
###ax = fig.add_subplot(1, 1, 1)
##ax.spines['left'].set_position('center')
##ax.spines['bottom'].set_position('center')
##ax.spines['right'].set_color('none')
##ax.spines['top'].set_color('none')
##ax.xaxis.set_ticks_position('bottom')
##ax.yaxis.set_ticks_position('left')

plt.xlabel('x - axis')
plt.ylabel('y - axis')

# plot the function
plt.plot(x,y, 'g')

plt.grid()
plt.axvline(x=0, c="red", label="x=0")
plt.axhline(y=0, c="yellow", label="y=0")

# show the plot
plt.show()




##class g():
##    def __init__(self,coor):
##        
