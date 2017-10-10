from numpy import*
from LeastSqure import*

def GradientDescentAddRegular(x,y,w_init):
    reg=0.0005
    new_w = mat(w_init.copy()).T
    Y = mat(y).T
    step = 0.0625;
    X = mat(zeros((x.size, w_init.size)))
    for i in range(x.size):
        for j in range(w_init.size):
            X[i, j] = pow(x[i], j)
    old_w = new_w.copy()
    new_w = new_w - step * (dot(X.T, (dot(X, old_w) - Y))+reg*old_w)
    new_w_n = 0.0
    print("new_w1:", array(new_w.T)[0])
    for i in range(x.size):
        new_w_n += pow((polynomial(x[i], array(new_w.T)[0]) - y[i]), 2)
    new_w_n /= 2
    new_w_n +=dot(new_w.T,new_w)[0,0]*reg/2
    n = 0
    while (new_w_n > 0.05 and n < 200000):
        old_w = new_w.copy()
        n = n + 1
        new_w -= step * (dot(X.T, (dot(X, old_w) - Y))+reg*old_w)
        old_w_n=new_w_n.copy()
        new_w_n = 0.0
        for i in range(x.size):
            new_w_n += pow((polynomial(x[i], array(new_w.T)[0]) - y[i]), 2)
        new_w_n /= 2
        new_w_n += dot(new_w.T, new_w)[0, 0] * reg / 2
        if old_w_n<new_w_n:
            step/=2
    w = zeros(w_init.size)
    for i in range(w_init.size):
        w[i] = new_w[i, 0]
    new_w_n = 0.0
    for i in range(x.size):
        new_w_n += pow((polynomial(x[i], array(new_w.T)[0]) - y[i]), 2)
    new_w_n /= 2
    #new_w_n += dot(new_w.T, new_w)[0, 0] * reg / 2
    return w
    
def GradientDescentInMatrix(x,y,w_init):
    new_w=mat(w_init.copy()).T
    Y=mat(y).T
    step=0.0625;
    X = mat(zeros((x.size, w_init.size)))
    for i in range(x.size):
        for j in range(w_init.size):
            X[i, j] = pow(x[i], j)
    #old_w=new_w.copy();
    new_w=new_w-step*dot(X.T,(dot(X,new_w)-Y))
    new_w_n=0.0
    for i in range(x.size):
        new_w_n+=pow((polynomial(x[i],array(new_w.T)[0])-y[i]),2)
    new_w_n/=2
    n=0
    while(new_w_n>0.05 and n<200000):
        n=n+1
        new_w -= step * dot(X.T, (dot(X, new_w) - Y))
        old_w_n=new_w_n.copy()
        new_w_n=0.0
        for i in range(x.size):
            new_w_n += pow((polynomial(x[i], array(new_w.T)[0]) - y[i]), 2)
        new_w_n/=2
        if old_w_n<new_w_n:
            step/=2
    w=zeros(w_init.size)
    for i in range(w_init.size):
        w[i]=new_w[i,0]
    new_w_n = 0.0
    for i in range(x.size):
        new_w_n += pow((polynomial(x[i], array(new_w.T)[0]) - y[i]), 2)
    new_w_n /= 2
    return w