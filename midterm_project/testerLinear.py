######################################################################
### OBJECT ORIENTED PROGRAMMING - MIDTERM PROJECT

###############
# Import Libraries required
from DataSet import *
from models_commented import *
from diagnosticPlot import *
import statsmodels.api as sm
###############
## LOAD DATA
# Load the Real Estate csv Data Set using the csvDataSet class and scale it and add constant
dataTest = csvDataSet("real_estate.csv", horizontal_x = False, scale = True, headers = False)
dataTest.add_constant()

###############
## CREATE A LINEAR REGRESSION OBJECT AND USE ITS METHODS
# Define and fit model parameters for various models
linearRegression_1 = LinearRegression(dataTest.x, dataTest.y, horizontal_x = True)
linearRegression_1.linearModel("y ~ b0 + b1*x2 + b2*x3 + b3*x4")
linearRegression_1.optimize()
linearRegression_1.summary()
# Use the diagnosticPlot class to plot the results of the logistic regression
diagnostic_1 = diagnosticPlot(linearRegression_1)
diagnostic_1.plot(linearRegression_1.y, linearRegression_1.predict(linearRegression_1.params, linearRegression_1.x))


linearRegression_2 = LinearRegression(dataTest.x, dataTest.y, horizontal_x = True)
linearRegression_2.linearModel("y ~ b0 + b1*x1 + b2*x2 + b3*x3 + b4*x4 + b5*x5")
linearRegression_2.optimize()
linearRegression_2.summary()
# Use the diagnosticPlot class to plot the results of the logistic regression
diagnostic_2 = diagnosticPlot(linearRegression_2)
diagnostic_2.plot(linearRegression_2.y, linearRegression_2.predict(linearRegression_2.params, linearRegression_2.x))

###############
## LOAD DATA
# Load the Real Estate csv Data Set using the csvDataSet class and scale it
dataTest = csvDataSet("real_estate.csv", horizontal_x = False, scale = True, headers = False)

linearRegression_3 = LinearRegression(dataTest.x, dataTest.y, horizontal_x = True, intercept = False)
linearRegression_3.linearModel("y ~ b1*x1")
linearRegression_3.optimize()
linearRegression_3.summary()
# Use the diagnosticPlot class to plot the results of the logistic regression
diagnostic_3 = diagnosticPlot(linearRegression_3)
diagnostic_3.plot(linearRegression_3.y, linearRegression_3.predict(linearRegression_3.params, linearRegression_3.x))

