######################################################################
### FINAL HOMEWORK ASSIGNMENT

# Import argparse library
import argparse

# define parser
parser = argparse.ArgumentParser(description = "A logistic regression on the statsmodels spector dataset", epilog = "Please specify only one of the train or test arguments.")

# add arguments
parser.add_argument("-s", "--seed", type = int, metavar = "", required = False, default = 12345, help = "random seed for train-test split" )

group = parser.add_mutually_exclusive_group(required = True)
group.add_argument("-tr", "--train", type = float, metavar="", help = "train set as a percentage of total data")
group.add_argument("-te", "--test", type = float, metavar="", help = "test set as a percentage of total data")

parser.add_argument("-c", "--covariates", type = str, metavar = "", default ="y ~ b0 + b1*x1", choices = ["y ~ b0","y ~ b0 + b1*x1","y ~ b0 + b1*x1 + b2*x2","y ~ b0 + b1*x1 + b2*x3","y ~ b0 + b1*x2 + b2*x3","y ~ b0 + b1*x1 + b2*x2 + b3*x3"], help = "specify the model" )
parser.add_argument("-mp", "--make_plot", action = "store_true", help = "call to create plot of model")
args = parser.parse_args()
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
if args.train is not None:
    dataTest.train_test(trainSize = args.train, randomSeed = args.seed)
else:
    dataTest.train_test(trainSize = 1-args.test, randomSeed = args.seed)

###############
## CREATE A LOGISTIC REGRESSION OBJECT AND USE ITS METHODS
# expression
logRegression = LogisticRegression(dataTest.x_tr, dataTest.y_tr, horizontal_x = True, intercept = ("b0" in args.covariates))
logRegression.linearModel(args.covariates)
logRegression.optimize(init_val=1)
logRegression.summary()
# Use the diagnosticPlot class to plot the results of the logistic regression
if args.make_plot:
    if "b0" in args.covariates:
        diagnostic_1 = diagnosticPlot(logRegression)
        test = [0]+[int(args.covariates[i+1]) for i in range(len(args.covariates)) if args.covariates[i] == "x"]
        test = dataTest.x_te[test,:]
        diagnostic_1.plot(dataTest.y_te, logRegression.predict(logRegression.params, test))
    else:
        diagnostic_1 = diagnosticPlot(logRegression)
        test = [int(args.covariates[i+1]) for i in range(len(args.covariates)) if args.covariates[i] == "x"]
        test = dataTest.x_te[test,:]
        diagnostic_1.plot(dataTest.y_te, logRegression.predict(logRegression.params, test))
    






