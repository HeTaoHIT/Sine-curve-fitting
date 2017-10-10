from numpy import*
from scipy import optimize

def polynomial(x,w):
    answer=0.0
    for i in range(w.size):
        answer+=w[i]*pow(x,i)
    return answer

def leastSqure(xone,y,w_init):
    X=mat(zeros((xone.size, w_init.size)))
    for i in range(xone.size):
        for j in range(w_init.size):
            X[i,j]=pow(xone[i],j)
    #w=(((X.T)*X).I)*(X.T)*y
    w=zeros(w_init.size)
    for i in range(w_init.size):
        w[i]=dot(dot(dot(X.T,X).I,X.T),y)[0,i]
    #w=X.T*X
    print("w: ",w)
    return w

    