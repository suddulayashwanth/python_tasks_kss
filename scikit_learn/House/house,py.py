# Project Title: KC House Price Prediction
# Import required libraries
import numpy as np
import pandas as pd

# Scenario 1: Load dataset
dataset=pd.read_csv("kc_house_data.csv")

# Select required features without id and date
features=["bedrooms","bathrooms","sqft_living","sqft_lot","floors","waterfront","view","condition","grade","sqft_above","sqft_basement","yr_built","yr_renovated","zipcode","lat","long","sqft_living15","sqft_lot15"]

print("First 5 Rows:")
print(dataset[features+["price"]].head())
print("\nSelected Columns:")
print(features+["price"])

# Scenario 2: Select features and target
X=dataset[features].values
y=dataset["price"].values

print("-"*80)
print(f"Shape of X is {X.shape}")
print(f"Shape of y is {y.shape}")

# Scenario 3: Split training and testing data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

print("-"*80)
print(f"Length of X_train: {len(X_train)}")
print(f"Length of X_test: {len(X_test)}")
print(f"Length of y_train: {len(y_train)}")
print(f"Length of y_test: {len(y_test)}")

# Scenario 4: Handle missing values
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(strategy="median")
X_train=imputer.fit_transform(X_train)
X_test=imputer.transform(X_test)

print("-"*80)
print("Missing values in X_train:",np.isnan(X_train).sum())
print("Missing values in X_test:",np.isnan(X_test).sum())

# Scenario 5: Feature scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train_scaled=sc.fit_transform(X_train)
X_test_scaled=sc.transform(X_test)

# Import evaluation metrics
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

# Model evaluation function
def evaluate_model(model_name,y_actual,y_prediction):
    mae=mean_absolute_error(y_actual,y_prediction)
    mse=mean_squared_error(y_actual,y_prediction)
    rmse=np.sqrt(mse)
    r2=r2_score(y_actual,y_prediction)
    print("\n"+"-"*80)
    print(model_name)
    print("Mean Absolute Error:",round(mae,2))
    print("Mean Squared Error:",round(mse,2))
    print("Root Mean Squared Error:",round(rmse,2))
    print("R² Score:",round(r2,4))
    print("Accuracy Percentage:",f"{r2*100:.2f}%")

# Scenario 6: Linear Regression
from sklearn.linear_model import LinearRegression
linear_model=LinearRegression()
print("\nLinear Regression Model:")
print(linear_model)
linear_model.fit(X_train_scaled,y_train)
linear_prediction=linear_model.predict(X_test_scaled)
evaluate_model("Linear Regression Results",y_test,linear_prediction)

# Scenario 7: Support Vector Regression
from sklearn.svm import SVR
svr_model=SVR(kernel="rbf",C=100000,epsilon=1000)
print("\nSupport Vector Regression Model:")
print(svr_model)
svr_model.fit(X_train_scaled,y_train)
svr_prediction=svr_model.predict(X_test_scaled)
evaluate_model("Support Vector Regression Results",y_test,svr_prediction)

# Scenario 8: K-Nearest Neighbors Regression
from sklearn.neighbors import KNeighborsRegressor
knn_model=KNeighborsRegressor(n_neighbors=5)
print("\nK-Nearest Neighbors Regression Model:")
print(knn_model)
knn_model.fit(X_train_scaled,y_train)
knn_prediction=knn_model.predict(X_test_scaled)
evaluate_model("K-Nearest Neighbors Results",y_test,knn_prediction)

# Scenario 9: Decision Tree Regression
from sklearn.tree import DecisionTreeRegressor
decision_tree_model=DecisionTreeRegressor(random_state=0)
print("\nDecision Tree Regression Model:")
print(decision_tree_model)
decision_tree_model.fit(X_train,y_train)
decision_tree_prediction=decision_tree_model.predict(X_test)
evaluate_model("Decision Tree Regression Results",y_test,decision_tree_prediction)

# Scenario 10: Random Forest Regression
from sklearn.ensemble import RandomForestRegressor
random_forest_model=RandomForestRegressor(n_estimators=100,random_state=0,n_jobs=-1)
print("\nRandom Forest Regression Model:")
print(random_forest_model)
random_forest_model.fit(X_train,y_train)
random_forest_prediction=random_forest_model.predict(X_test)
evaluate_model("Random Forest Regression Results",y_test,random_forest_prediction)

# Scenario 11: Gradient Boosting Regression
from sklearn.ensemble import GradientBoostingRegressor
gradient_model=GradientBoostingRegressor(random_state=0)
print("\nGradient Boosting Regression Model:")
print(gradient_model)
gradient_model.fit(X_train,y_train)
gradient_prediction=gradient_model.predict(X_test)
evaluate_model("Gradient Boosting Regression Results",y_test,gradient_prediction)

# Scenario 12: Compare all models
model_results=pd.DataFrame({
    "Model":["Linear Regression","Support Vector Regression","K-Nearest Neighbors","Decision Tree","Random Forest","Gradient Boosting"],
    "R2 Score":[
        r2_score(y_test,linear_prediction),
        r2_score(y_test,svr_prediction),
        r2_score(y_test,knn_prediction),
        r2_score(y_test,decision_tree_prediction),
        r2_score(y_test,random_forest_prediction),
        r2_score(y_test,gradient_prediction)
    ]
})

model_results=model_results.sort_values(by="R2 Score",ascending=False)
print("\n"+"-"*80)
print("Model Comparison:")
print(model_results)

best_model=model_results.iloc[0]
print("\nBest Model:",best_model["Model"])
print("Best R² Score:",round(best_model["R2 Score"],4))