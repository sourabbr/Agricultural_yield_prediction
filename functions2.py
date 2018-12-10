import numpy as np
import matplotlib.pyplot as plt
from regression import Regression

def featureNormalize(x):
    mean=np.mean(x)
    stddev=np.std(x)
    X_norm=(np.array(x)-mean)/stddev
    X_norm=X_norm.tolist()
    return(X_norm)

def predict(xlabel,ylabel,x_val,x,y):
    meanx=np.mean(x)
    stddevx=np.std(x)
    meany=np.mean(y)
    stddevy=np.std(y)
    x=featureNormalize(x)
    y=featureNormalize(y)

    reg = Regression()
    reg.set_learning_rate(0.001)
    reg.set_max_iterations(10000)
    reg.set_l1_penalty(0.1)
    reg.set_l2_penalty(0.1)
    reg.set_tolerance(1e-5)
    theta, cost, it = reg.polynomial_regression(x, y, 5)

    z = np.linspace(-1.9, 2.1, 4/0.01)
    prediction = reg.predict(z)

    x=np.array(x)*stddevx+meanx
    z=np.array(z)*stddevx+meanx
    y=np.array(y)*stddevy+meany
    prediction=np.array(prediction)*stddevy+meany

    x_val=(x_val-meanx)/stddevx
    y_val=reg.predict([x_val])
    x_val=[x_val]
    x_val=np.array(x_val)*stddevx+meanx
    y_val=np.array(y_val)*stddevy+meany

    fig = plt.figure(figsize=(4,4))
    plt.plot(x,y,'.', label='Input data')
    plt.plot(z,prediction,'r-', label='Best fit curve')
    plt.plot(x_val,y_val,'gx',label='Predicted Data')
    plt.legend(loc=4)
    title=xlabel + " vs " + ylabel
    plt.title(title,size=10)
    plt.xticks(size=8)
    plt.yticks(size=8)
    plt.close('all')

    return([y_val,fig])

def predict2(x_val,x,y):
    meanx=np.mean(x)
    stddevx=np.std(x)
    meany=np.mean(y)
    stddevy=np.std(y)
    x=featureNormalize(x)
    y=featureNormalize(y)

    reg = Regression()
    reg.set_learning_rate(0.001)
    reg.set_max_iterations(10000)
    reg.set_l1_penalty(0.1)
    reg.set_l2_penalty(0.1)
    reg.set_tolerance(1e-5)
    theta, cost, it = reg.polynomial_regression(x, y, 5)

    x_val=(x_val-meanx)/stddevx
    y_val=reg.predict([x_val])
    y_val=np.array(y_val)*stddevy+meany

    return(y_val)

def NormalEquation(x_val,y,*x):
    m=len(y)
    y=(np.array([y])).transpose()
    X=np.ones((m,1))
    for i in x:
        temp=(np.array([i])).transpose()
        X = np.hstack([X,temp])
    n=(X.shape)[1]
    theta=np.zeros((n,1))
    theta=(np.linalg.inv(X.transpose().dot(X))).dot(X.transpose().dot(y))
    x_val2=np.empty((1,n))
    x_val2[0,0]=1
    for i in range(len(x_val)):
        x_val2[0,i+1]=x_val[i]
    y_val=x_val2.dot(theta)
    return(y_val[0,0])
