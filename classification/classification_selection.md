# Model Selection  

**Models:** 


* Logistic (Binary or Ordinal)
```
Logistic regression is a linear equation that has a sigmoid function applied to the output to make the values fit between 0 and 1.  Traditional logisitic regression does not use regularization and maximizes the sum of squared residuals (errors).  Packages like scikit-learn use a regularized version that applies a L2 penality (ridge) - this minimizes the linear equation coefficients.  This algorithm does not have the same assumptions as linear regression.  Linearity, normality of errors, homoscedasticity, and features being continuous are not required.  The data should be independent (not repeated measurements), lack multicollinearity, feature(s) are related to the log odds, and the number of samples has at least 10 cases for each independent variable divided by the proportion of the minority class of the entire dataset (or overfitting is more likely).  Similar to linear regression, logistic regression has difficulty to handling large numbers of categorical features and should be limited to two-class classification.  
```  

* KNN  
```
K-Nearest Neighbors is an algorithm that selects the nearest data points to the defined point.  The point is classified based on the highest class probability.  The distance function can be modified based on the type of problem.  For example, if coordinates are used then the haversine distance will calculate distance including the curvature of the earth.  For simple straight line distances then euclidean distance is simple and easy to calculate.  Since the measurement of distances is based on a distance that is composed of feature distances and features scales could cause a bias of over-prioritizing a feature, all features should be scaled similarly.  Standard scaler is probably the most common way of scaling but Min-Max Scaler could work under certain situations.  Although k needs to be defined, by testing many k-values the upper and lower limits can be determined based on the error.  KNN is particularly helpful when there is limited data and the data is found in radial clusters.  It is particularly helpful when trying to fill in incomplete data but to make a binary prediction, the k-value should be an odd number so no ties can occur.  
```

* Decision Trees
* Random Forest  
* Isolation Forest - identifies early terminating branches as outliers

* Support Vector Classifier 

* Naive Bayes (text)
* Gaussian Naive Bayes (continuous data)


* Gradient Boosting
* Linear Discriminant Learning
* Quadratic Discriminant Learning




 