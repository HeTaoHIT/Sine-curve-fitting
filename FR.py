from numpy import *
from GradientDescent import *

def daoF(X,Y,x,N):
    answer=(dot(dot(X.T,X),x)-dot(X.T,Y))
    return answer

def d1Size(X):
    s=0.0
    for i in range(X.size):
        s+=pow(X[i,0],2)
    return s

def generateUnitMatrix(size):
    a=zeros((size,size))
    for i in range(size):
        a[i,i]=1
    return mat(a)

def FR(x,y,w_init):
    w=mat(w_init.copy()).T
    Y=mat(y.copy()).T
    X = mat(zeros((x.size, w_init.size)))
    for i in range(x.size):
        for j in range(w_init.size):
            X[i, j] = pow(x[i], j)
    A=dot(X.T,X)
    g=daoF(X,Y,w,x.size)
    if(d1Size(g)!=0):
        d=-g
        n=1
        while(d1Size(g)>0.00000001):
            step=(dot(-g.T,d)/dot(dot(d.T,A),d))[0,0]
            w+=step*d
            g=daoF(X,Y,w,x.size)
            speed=(dot(dot(d.T,A),g)/dot(dot(d.T,A),d))[0,0]
            d=-g+speed*d
            n+=1
    new_w=zeros(w_init.size)
    print("size(g):",d1Size(g))
    print("n:",n)
    for i in range(w_init.size):
        new_w[i]=w[i,0]
    return new_w

def FRAddRegular(x,y,w_init):
    rg=0.1
    w=mat(w_init.copy()).T
    Y=mat(y.copy()).T
    X = mat(zeros((x.size, w_init.size)))
    for i in range(x.size):
        for j in range(w_init.size):
            X[i, j] = pow(x[i], j)
    E = generateUnitMatrix(w_init.size)
    A=dot(X.T,X)+E*rg
    g=daoF(X,Y,w,x.size)
    if(d1Size(g)!=0):
        d=-g
        n=0
        while(d1Size(g)>0.000001):
            step=(dot(-g.T,d)/dot(dot(d.T,A),d))[0,0]
            w+=step*d
            g=daoF(X,Y,w,x.size)
            speed=(dot(dot(d.T,A),g)/dot(dot(d.T,A),d))[0,0]
            d=-g+speed*d
            n+=1
    new_w=zeros(w_init.size)
    print("reg n:",n)
    for i in range(w_init.size):
        new_w[i]=w[i,0]
    return new_w

