import numpy as np

class Regression:
    
    def __init__(self):
        self.max_iter = 1000
        self.learning_rate = 0.01
        self.order = 1
        self.theta = np.zeros(2)
        self.l1_penalty = 0
        self.l2_penalty = 0
        self.tolerance = 1e-4

    def set_max_iterations(self, iterations):
        self.max_iter = iterations
    
    def set_learning_rate(self, alpha):
        self.learning_rate = float(alpha)
    
    def set_l2_penalty(self, l2_coeff):
        self.l2_penalty = float(l2_coeff)
        
    def set_l1_penalty(self, l1_coeff):
        self.l1_penalty = float(l1_coeff)
    
    def set_tolerance(self, tol):
        self.tolerance = float(tol)
        
    def polynomial_regression(self, x, y, deg):
        self.order = deg+1
        features = np.empty([len(x), self.order], dtype=float)
        self.theta = np.zeros(self.order)
        cost_prev = 0
        
        for i in range(len(x)):
            for p in range(self.order):
                features[i][p] = pow(x[i], p)
    
        log = 0
        for repeat in range(self.max_iter):
            mat_mult = (features.dot(self.theta) - y)
            self.theta[0] -= (self.learning_rate/len(x))*(mat_mult*features[:,0]).sum()
            for j in range(1, self.order):
                self.theta[j] -= (self.learning_rate/len(x))*((mat_mult*features[:,j]).sum() 
                                                              + self.l1_penalty + self.l2_penalty*self.theta[j])
            if(repeat%10 == 0):
                cost = (1./(2*len(x))) * (np.power(features.dot(self.theta) - y, 2).sum() 
                                                  + self.l1_penalty*self.theta.sum() 
                                                  + self.l2_penalty*np.power(self.theta,2).sum())
                if(log > 1 and np.abs(cost - cost_prev) < self.tolerance):
                    break
                log += 1
                cost_prev = cost
    
        return (self.theta, cost, repeat)
    
    def linear_regression(self,x,y):
        return (self.polynomial_regression(x, y, 1))
    
    def predict(self,x):
        result = np.zeros(len(x))
        for i in range(self.order):
            result += self.theta[i]*np.power(x,i)
        return (result)
    
