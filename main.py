import numpy as np
import matplotlib.pyplot as plot
import GeneratorData as gd
import LeastSqure as LS
import GradientDescent as GD
import FR

size=10
x,y=gd.getGaussionData(size)

for i in range(size):
    plot.scatter(x[i],y[i],color="green", linewidths=0.01)

rank=10
x_points=np.linspace(0,1,num=1000)
w_init=np.random.randn(rank)
print("x",x)
print("y",y)
print("w_init:",w_init)

plot.title("y=sin(x)")
plot.plot(x_points,np.sin(2*np.pi*x_points),label='$sin(2*math.pi)$',color="red")
plot.xlabel('x-coordinate')
plot.ylabel('y-coordinate')

'''w_LS1=LS.leastSqure(x,y,w_init)
print("w_LS1:",w_LS1)
plot.plot(x_points,LS.polynomial(x_points,w_LS1),label= 'least square method',color="yellow")'''

'''w_GD1=GD.GradientDescentInMatrix(x,y,w_init)
print("w_GD1:",w_GD1)
plot.plot(x_points,LS.polynomial(x_points,w_GD1),label='GradientDescent' ,color="blue")

w_GD2=GD.GradientDescentAddRegular(x,y,w_init)
print("w_GD2:",w_GD2)
plot.plot(x_points,LS.polynomial(x_points,w_GD2),label= 'GradientDescent + regular terms',color="black")'''

w_FR1=FR.FR(x,y,w_init)
print("w_FR1:",w_FR1)
plot.plot(x_points,LS.polynomial(x_points,w_FR1),label= "FR",color="blue")

w_FR2=FR.FRAddRegular(x,y,w_init)
print("w_FR2:",w_FR2)
plot.plot(x_points,LS.polynomial(x_points,w_FR2),label= "FR + regular items",color="black")

plot.legend()
plot.show()
#plot.savefig()





