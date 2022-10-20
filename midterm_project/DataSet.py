######################################################################
### OBJECT ORIENTED PROGRAMMING - MIDTERM PROJECT

###############
# Import Libraries required
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import random
import math
import csv

###############
## This module defines a superclass that models a DataSet.
#
class DataSet : # Superclass
          
    #####  
    ## Constructs a DataSet object which contains x and y arrays. It adjusts them (transpose or scale) so that they can be processed by a linear model. 
    # @param x are the covariates entered by the user as a numpy array
    # @param y is the dependent variable entered by the user as a numpy array
    # @param scale is a boolean variable that indicates whether the array inputs (x and y) should be scaled
    # @param horizontal_x is a boolean variable that indicates whether the input array x contains row vectors
    #
    def __init__(self, x, y, horizontal_x = False, scale = False) :
        # Validate that the inputs x and y are numpy arrays
        if isinstance(x, np.ndarray) == False or isinstance(y, np.ndarray) == False :
            raise TypeError("The inputs x and y must be of the type numpy array!")
       
        # Validate that the arrays y and x have the same length
        if horizontal_x == False and len(x) != len(y) :
            raise ValueError("The arrays x and y must have the same number of observations!")        
        elif horizontal_x == True and len(np.transpose(x)) != len(y) :
            raise ValueError("The arrays x and y must have the same number of observations!")
       
        self._x = x
        self._y = y

        # Scale the x array according to the user guidelines
        if scale == True :
            # Create a MinMaxScaler object from the sklearn.preprocessing package
            scaler = MinMaxScaler()
            
            if horizontal_x == False :
                #Scale the variable x
                self._x = scaler.fit_transform(self._x)
            else :           
                #Scale the variable x
                self._x = np.transpose(scaler.fit_transform(np.transpose(self._x)))
                
        # Transpose the x array according to the user guidelines
        if horizontal_x == False :
            self._x = np.transpose(self._x)


    #####  
    ## Appends a vector of 1s in the first row of the x array.
    # 
    def add_constant(self) :
        # Generate a vector of 1s
        vector = np.ones((np.shape(self._x)[1],1), dtype=int)
        # Append the 1s vector to the x array
        self._x = np.transpose(np.append(vector, np.transpose(self._x), axis=1)) 

    #####  
    ## Randomly splits the y and x arrays into train and test in accordance with the split (percentage of train data) and the random seed specified by the user
    # @param trainSize is the percentage of data that will be part of the train set 
    # @param randomSeed is the number of theseed used to split the data according to the train size  
    #      
    def train_test(self, trainSize = 0.7, randomSeed = 1234) :
        # Set a random seed for the sample
        random.seed(randomSeed)               
        self._x = np.transpose(self._x)           
           
        # Draw a random sample for the training set
        sample_tr = random.sample(range(len(self._y)), math.floor(len(self._y)*0.7))
        sample_te = np.setdiff1d(range(len(self._y)), sample_tr, assume_unique=False)
           
        self._x_tr = self._x[sample_tr]
        self._x_te = self._x[sample_te]
        self._y_tr = self._y[sample_tr]
        self._y_te = self._y[sample_te]

        # Original and new arrays are transposed
        self._x = np.transpose(self._x)                  
        self._x_tr = np.transpose(self._x_tr) 
        self._x_te = np.transpose(self._x_te)

    #####  
    ## Allows the user to get the x array.
    # @return is a numpy array with the x array 
    #     
    @property # use of decorators
    def x(self) :
        return self._x
    
    #####  
    ## Allows the user to set the x array.
    #     
    @x.setter # use of decorators
    def x(self, x) :
       # Validate that the variable x is a numpy array
       if isinstance(x, np.ndarray) == False :
           raise TypeError("The input must be of the type numpy array!")  
       else :
           # Validate that the arrays y and x have the same length
           if len(self._y) != len(x) :
               raise TypeError("The arrays y and x must have the same length!")
           else :
               self._x = x
   
    #####  
    ## Allows the user to get the y array.
    # @return is a numpy array with the y array 
    #
    @property # use of decorators        
    def y(self) :
       return self._y
   
    #####  
    ## Allows the user to set the y array.
    #     
    @y.setter # use of decorators
    def y(self, y) :
       # Validate that the variable x is a numpy array
       if isinstance(y, np.ndarray) == False :
           raise TypeError("The input must be of the type numpy array!") 
       
       # Validate that the arrays y and x have the same length
       if len(y) != len(self._x) :
           raise TypeError("The arrays y and x must have the same length!")
       else :
           self._y = y    
      
    #####  
    ## Allows the user to get the training sample for the x array.
    # @return is a numpy array with the training sample for the x array
    # 
    @property # use of decorators         
    def x_tr(self) :
       return self._x_tr
   
    #####  
    ## Allows the user to get the training sample for the y array.
    # @return is a numpy array with the training sample for the y array
    #      
    @property # use of decorators   
    def y_tr(self) :
       return self._y_tr

    #####  
    ## Allows the user to get the test sample for the x array.
    # @return is a numpy array with the test sample for the x array
    #
    @property # use of decorators          
    def x_te(self) :
       return self._x_te
   
    #####  
    ## Allows the user to get the test sample for the y array.
    # @return is a numpy array with the test sample for the y array
    # 
    @property # use of decorators      
    def y_te(self) :
       return self._y_te


###############
## This module defines a subclass that models a csv DataSet.
#
class csvDataSet(DataSet) : # Subclass
    
    #####  
    ## Constructs a csvDataSet object which reads a csv file, creates y and x arrays and adjusts them (transpose or scale) so that they can be processed. 
    # @param y is the dependent variable entered by the user as a numpy array
    # @param x are the covariates entered by the user as a numpy array
    # @param scale is a boolean variable that indicates whether the data inputs (y and x) should be scaled
    # @param horizontal_x is a boolean variable that indicates whether the arrays (y and x) must be transposed. When using csvDataSet the default is true
    # @param headers is a boolean variable that indicates whether the csv file contains headers on the first row   
    #
    def __init__(self, filename, horizontal_x = True, scale = False, headers = False) :
       raw_data = open(filename, "rt")
       reader = csv.reader(raw_data, delimiter=",", quoting=csv.QUOTE_NONE)
       data = list(reader)
       data = np.array(data, dtype = np.float32)

       # Extract the first column as the y array and the rest as the x array
       if headers == True :           
           x = np.array(data[1:,1:])
           y = np.array(data[1:,0])
       else :
           x = np.array(data[0:,1:])
           y = np.array(data[0:,0])
            
       # Use the Superclass constructor
       super().__init__(x, y, horizontal_x, scale)


