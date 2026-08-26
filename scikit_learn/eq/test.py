# Import the libraries
from random import randint
from sklearn.linear_model import LinearRegression
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100
# Create an empty list of the input training set 'X' and create an empty list of the
TRAIN_INPUT = list()
TRAIN_OUTPUT= list()
#Create and append a randomly generated data set to the input and output
for i in range(TRAIN_SET_COUNT):
 a = randint(0, TRAIN_SET_LIMIT)
 b = randint(0, TRAIN_SET_LIMIT)
 c = randint(0, TRAIN_SET_LIMIT)
 #Create a linear function for the output dataset 'Y'
 op = (10*a) + (2*b) + (3*c)
 TRAIN_INPUT.append([a,b,c])
 TRAIN_OUTPUT.append(op)
predictor = LinearRegression(n_jobs=-1) 
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)
X_TEST = [[10,20,30]] 
outcome = predictor.predict(X=X_TEST) 
coefficients = predictor.coef_ 
print('Outcome: {} \n Coefficients: {}'.format(outcome, coefficients))