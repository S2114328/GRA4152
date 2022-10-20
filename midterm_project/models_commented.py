######################################################################
### OBJECT ORIENTED PROGRAMMING - MIDTERM PROJECT

###############
# Import Libraries required
import numpy as np
from scipy.optimize import minimize
from sklearn.metrics import roc_auc_score

###############
## This module defines a superclass LM that generates regression models (linear and logistic).
#
class LM : # Superclass
        
    #####
    ## Constructs an LM object which contains x and y arrays. It adjusts them (transpose) so that they can be processed. 
    # @param x are the covariates entered by the user as a 2D numpy array
    # @param y is the dependent variable entered by the user as a numpy array
    # @param horizontal_x is a boolean variable that indicates whether the input parameter x contains row vectors
    # @param intercept is a boolean variable that is True when the input x contains an intercept row/column
    #
    def __init__(self, x, y, horizontal_x = True, intercept = True):
        # Validate that the inputs x and y are numpy arrays
        if isinstance(x, np.ndarray) == False or isinstance(y, np.ndarray) == False :
            raise TypeError("The inputs x and y must be of the type numpy array!")
        # Y must be a 1D numpy array
        y = y.flatten()
        # Validate that the arrays y and x have the same length
        if horizontal_x == True and x.shape[1] != y.shape[0] :
            raise ValueError("The arrays x and y must have the same number of observations!")        
        if horizontal_x == False and x.shape[0] != y.shape[0] :
            raise ValueError("The arrays x and y must have the same number of observations!")
        # Store y    
        self._y = y
        # Store whether intercept in design matrix
        self._intercept = intercept
        # Transpose the variable x according to the user guidances
        if horizontal_x == False:
            self._covariates = np.transpose(x)
        else:
            self._covariates = x
            
        self._nparam = 0
    
    #####  
    ## Identifies the dependent variable and the covariates given by the user in a string with a linear model. 
    # @param model is a string that specifies a linear model with the dependent variable and the covariates
    #     
    def linearModel(self, model):
        # Validate that the model is a string
        if isinstance(model, str) == False :
            raise TypeError("The model must be a string!") 
        
        self._model = model
        
        # Identify the number of parameters (betas) to calculate the deviance
        self._nparam = model.count("b")
        
        # Extract rows required by model and save variable names
        if self._intercept == True:
            m = model.split("x")[1:]
            m.insert(0,"0")
            self._x = self._covariates[[int(i[0]) for i in m], : ]
        else:
            self._x = self._covariates[[int(i[0])-1 for i in model.split("x")[1:]], : ]
        
        # Creates empty parameter array    
        self._param = np.array(np.zeros(self._nparam))
    
    #####  
    ## Abstract class to calculate the deviance. 
    # @param param is the parameters (betas) for the deviance
    #   
    def fit(self, param, x, y) :
        # To be specified
        raise NotImplementedError
    
    #####  
    ## Abstract class to predict y_hat using current parameter estimates. 
    # @return is the prediction (y_hat) provided by the model
    # 
    def predict(self, param, x):
        # To be specified
        raise NotImplementedError
    
    #####  
    ## Numerically minimizes the fit function/deviance
    # @param param is the parameters (betas) for the deviance
    # 
    def optimize(self, init_val = 1) :
        # Define starting parameters for the minimize function
        init_params = self._param + init_val
        # Minimize deviance
        results = minimize(self.fit, init_params, args = (self.x, self.y))
        # Store optimal parameters
        self._param = results["x"]
    
    #####  
    ## Allows the user to obtain the string representation of the current model
    # @return string with the current model
    #
    def model(self):
        ## loop through array replace b0 with first val
        out =  list(self._model)
        j=0
        for i in range(len(out)):
            if self._model[i] == "b":
                out[i] = ""
                out[i+1] = str(round(self.params[j],3))
                j+=1
        return "".join(out)    
        
    #####  
    ## Computes and returns a model performance metric depending on the model (linear or logistic regression)
    # @return string with the current model
    #
    def diagnosis(self):
        # To be specified
        raise NotImplementedError
    
    #####  
    ## Prints out a string with the fitted parameters. If the parameters have not been fitted, it prints the specified model with 0s in all parameters.
    # @return string with the fitter parameters or with 0s in case parameters have not been fitted
    #
    def __repr__(self):
        if self._nparam == 0:
            return "I am a LinearModel"
        else:
            return self.model()
    
    #####  
    ## Prints out the model specified in linearModel, the fitted parameters, and the model accuracy.
    #
    def summary(self):
        from tabulate import tabulate
        table = [["", 'Model Summary'],
                ["Model: ", self.model() ],
                ["Parameters: ", ", ".join([str(round(i,3)) for i in self._param]) ],
                ["Accuracy: ", self.diagnosis()]]
        print (tabulate(table, maxcolwidths=[None, 55]))
     
    #####  
    ## Allows the user to get the design array (x).
    # @return is a numpy array with the x array
    # 
    @property # use of decorators
    def x(self):
        return self._x  
    
    #####  
    ## Allows the user to get the y array (dependent variable).
    # @return is a numpy array with the y array
    # 
    @property # use of decorators 
    def y(self):
        return self._y
    
    #####  
    ## Allows the user to get the estimated parameters (betas).
    # @return is a numpy array with the parameters of the model
    # 
    @property # use of decorators
    def params(self):
        return self._param

###############
## This module defines a subclass that models a Linear Regression.
#
class LinearRegression(LM) : # Subclass

    #####  
    ## Constructs a LinearRegression object which contains x and y arrays. It adjusts them (transpose) so that they can be processed by a linear model. 
    # @param x are the covariates entered by the user as a numpy array
    # @param y is the dependent variable entered by the user as a numpy array
    # @param transpose_x is a boolean variable that indicates whether the data array x should be transposed
    # @param intercept is a boolean variable that is True when the input x contains an intercept row/column
    #
    def __init__(self, x, y, horizontal_x = True, intercept = True):
        # Use the Superclass constructor
        super().__init__(x, y, horizontal_x, intercept)
        
    #####  
    ## Method to calculate the deviance. 
    # @param params is the parameters (betas) for the deviance
    # @return is the deviance of the model 
    #     
    def fit(self, params, x, y):
              
        # Estimate y_hat
        miu  = self.predict(params, x)
        # Deviance
        dev = (self.y - miu)**2 
        return np.sum(dev)
    
    #####  
    ## Abstract class to predict y_hat using current parameter estimates. 
    # @return is the prediction (y_hat) provided by the model
    # 
    def predict(self, params, x):
        # Predict using the estimated parameters (betas)
        miu = np.matmul(np.transpose(x), params)
        return miu
        
    #####  
    ## Computes and returns the R2 of the linear regression
    # @return is the R2 of the linear regression
    #
    def diagnosis(self):
        D0 = np.sum((self.y - np.mean(self.y))**2)
        R2 = 1 - (self.fit(self.params, self.x, self.y) / D0)
        
        return round(R2,3)


###############
## This module defines a subclass that models a Logistic Regression.
#
class LogisticRegression(LM) : # Subclass

    #####  
    ## Constructs a LogisticRegression object which contains x and y arrays.  
    # @param x are the covariates entered by the user as a numpy array
    # @param y is the dependent variable entered by the user as a numpy array
    # @param transpose_x is a boolean variable that indicates whether the data array x should be transposed
    # @param intercept is a boolean variable that is True when the input x contains an intercept row/column
    #
    def __init__(self, x, y, horizontal_x = True, intercept = True):
        # Use the Superclass constructor
        super().__init__(x, y, horizontal_x, intercept)
    
    #####  
    ## Method to calculate the deviance. 
    # @param params is the parameters (betas) for the deviance
    # @return is the deviance of the model 
    # 
    def fit(self, params,x , y):
        # Calculate deviance
        t1 = np.log(1+np.exp(np.matmul(np.transpose(x), params)))
        t2 = np.matmul(np.transpose(x), params)
        dev = 0
        for i in range(len(y)):
            dev += t1[i]-y[i]*t2[i]
        return np.sum(dev)
    
    #####  
    ## Abstract class to predict y_hat using current parameter estimates. 
    # @return is the prediction (y_hat) provided by the model
    #
    def predict(self, params, x):
        # Predict using the estimated parameters (betas)
        miu = np.exp(np.matmul(np.transpose(x), params))/(1+np.exp(np.matmul(np.transpose(x), params)))
        return miu
        
    #####  
    ## Computes and returns the Area under the Curve (AUC) for the logistic regression
    # @return is the AUC for the logistic regression
    #
    def diagnosis(self):
        auc = roc_auc_score(self.y, self.predict(self.params, self.x))
        
        return round(auc,3)
    



