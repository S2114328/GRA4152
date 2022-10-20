######################################################################
### OBJECT ORIENTED PROGRAMMING - MIDTERM PROJECT

###############
# Import Libraries required
from models_commented import *
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

###############
## This module defines a class that models a diagnosticPlot for an object of the subclasses LinearRegression or LogisticRegression.
#
class diagnosticPlot : # Class
     
   #####  
   ## Constructs a diagnosticPlot object which identifies the type of Linear Model (LinearRegression or LogisticRegression). 
   # @param linearModel is an object of type LinearRegression or LogisticRegression
   #
   def __init__(self, linearModel) :
       # Validate that the input linearModel is an instance of the class LinearRegression or LogisticRegression
       if isinstance(linearModel, LinearRegression) == False and isinstance(linearModel, LogisticRegression) == False:
           raise TypeError("The input must be an instance of the LinearRegression or LogisticRegression classes!1")
       
       self._linearModel = linearModel

   #####  
   ## Builds a scatter plot of y against miu if the object is a LinearRegression. If the object is a Logistic Regression, it plots a ROC curve. 
   #             
   def plot(self, y, miu) :           
       # If the linearModel is an instance of the class LinearRegression, then we plot a scatterplot of y vs miu
       if isinstance(self._linearModel, LinearRegression) == True :
           plt.scatter(y, miu)
           plt.xlabel('$y$')
           plt.ylabel('$mu$')           
           plt.show()
           
       # If the linearModel is an instance of the class LogisticRegression, then we plot a ROC curve
       else :
           fpr, tpr, thresholds = metrics.roc_curve(y, miu)
           roc_auc = metrics.auc(fpr, tpr)
           display = metrics.RocCurveDisplay(fpr = fpr, tpr = tpr, roc_auc = roc_auc, estimator_name ='ROC curve')
           display.plot()
           plt.show()
 
           
           
           