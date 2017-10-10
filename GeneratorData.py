from numpy import*

def getGaussionData(size=10):
    gausError=random.normal(0,0.13,size)
    gausError=gausError-gausError.sum(axis=0)/size
    x=random.rand(size)
    x=sort(x)
    y=sin(2*pi*x)
    return x,y+gausError
