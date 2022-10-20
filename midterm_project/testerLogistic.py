######################################################################
### OBJECT ORIENTED PROGRAMMING - MIDTERM PROJECT

###############
# Import Libraries required
import statsmodels.api as sm
import numpy as np
from DataSet import *
from models_commented import *
from diagnosticPlot import *

###############
## LOAD DATA
# Load the Spector Data Set from Statsmodels and load the dependent variable and the covariates
spector_data = sm.datasets.spector.load()
x = np.array(spector_data.exog)
y = np.array(spector_data.endog)

###############
## CREATE A DATASET OBJECT AND USE ITS METHODS
# Create a DataSet object with the dependent variable and the covariates loaded from Statsmodels. 
dataTest = DataSet(x, y, horizontal_x = False, scale = False)
# add intercept
dataTest.add_constant()
# Create a train and test set using the seed value 12345 where the test data set contains 30% of the data
dataTest.train_test(trainSize = 0.7, randomSeed = 12345)

###############
## CREATE A LOGISTIC REGRESSION OBJECT AND USE ITS METHODS
# Define and fit model parameters for various models
logRegression_1 = LogisticRegression(dataTest.x_tr, dataTest.y_tr, horizontal_x = True)
logRegression_1.linearModel("y ~ b0 + b1*x1")
logRegression_1.optimize(init_val=1)
logRegression_1.summary()
# Use the diagnosticPlot class to plot the results of the logistic regression
diagnostic_1 = diagnosticPlot(logRegression_1)
diagnostic_1.plot(dataTest.y_te, logRegression_1.predict(logRegression_1.params, dataTest.x_te[0:2,:]))


logRegression_2 = LogisticRegression(dataTest.x_tr, dataTest.y_tr, horizontal_x = True)
logRegression_2.linearModel("y ~ b0 + b1*x1 + b2*x2")
logRegression_2.optimize(init_val=1)
logRegression_2.summary()
# Use the diagnosticPlot class to plot the results of the logistic regression
diagnostic_2 = diagnosticPlot(logRegression_2)
diagnostic_2.plot(dataTest.y_te, logRegression_2.predict(logRegression_2.params,dataTest.x_te[0:3,:])) 


logRegression_3 = LogisticRegression(dataTest.x_tr, dataTest.y_tr, horizontal_x = True)
logRegression_3.linearModel("y ~ b0 + b1*x1 + b2*x2 + b3*x3")
logRegression_3.optimize(init_val=1)
logRegression_3.summary()
# Use the diagnosticPlot class to plot the results of the logistic regression
diagnostic_3 = diagnosticPlot(logRegression_3)
diagnostic_3.plot(dataTest.y_te, logRegression_3.predict(logRegression_3.params, dataTest.x_te)) 







