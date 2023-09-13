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
```
A Decision Tree makes binary decisions to split each node into child nodes until there is a terminal node (also known as a leaf).  Each split maximizes the purity and calculated based on a metric.  Depending on the type of problem  we choose a different metric - for continuous target variables (regression) we use the 'Reduction in Variance' metric; for categorical target variables we use the gini impurity (probability squared), the information gain (aka entropy, log probability), or the chi-squared metric.  Gini is preferred because it is very similar to information gain but the algorithim performs better since it does not have a logorithm.  Entropy measures the amount of disorder so it is at its greatest when two class are equally probable.  On the other hand Gini is at its greatest when the probability of a class is at it's highest meaning it is at it's peak pureness.  The chi-squared metric is used if a node needs split by more than two categories.  Decision trees can be very precise but this also means that overfitting is very easy to do.  Here is a nice reference - [Link](https://quantdare.com/decision-trees-gini-vs-entropy/).  Improving the model can be done by changing thesholds related to the maximum number of branches (depth) the tree can have, the minimum number of samples in a node to allow a split, and the minimum number of samples in a terminating node.  Some less common constraints include the minimum weighted fraction of input weights to be a leaf and the maximum number of features considered when making a split.  The benefit of this model is that the outcomes can be viewed graphically and are easy to interpret.  

```
* Random Forest  
```
A random forest is an ensemble method that uses the most common output of many decision trees as its prediction for classification or it uses the average prediction of all the decision trees for regression.  This is also an example of a bagging process since the summarization of multiple models is occuring.  The benefit of this model include a lower probability of overfitting but lacks the graphical explanatory ability.  
```

* Isolation Forest
```
Isolation forests are a form of decision trees where early terminating branches are considered outliers (assumes anomalies are few and different).  This is an ensemble model and is also unsupervised model.  The features and data are randomly sampled and the samples that have the most depth are considered normal and the short depth are considered outliers.  
```

* Support Vector Classifier 
```
SVC are very good at solving binary classification problems, solving linear and non-linear problems, handling high dimensional spaces.  The downside is that the outcomes are more difficult to interpret.  The algorithm creates a decision boundary splitting the data.  With only two features it is a line but with more features it becomes a hyperplane. The distance between the hyperplane and the closest datapoint of each class make the decision margin which is what is being optimized.   [Ref](https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47) 
```

* Naive Bayes (text)  
```
Naive Bayes is used to stochastically group objects based on independent and equally significant features.  Objects are classified by Bayes Theorem where event A occurs at a particular probability given that B has occurred.  It is often used for text classification but the independence of features is often a faulty assumption.  It is liked due to its simplicity, need for little data, and effectiveness.  It is less reliable for regression due to the independence assumpiton.  There are several forms of NB.  Reference: [Link](https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c)  
```  

* Gaussian Naive Bayes (continuous data)
```
GNB is similar to regular NB but supports continuous features by conforming the variables to a Gausian Distribution.  Reference: [Link](https://www.analyticsvidhya.com/blog/2021/11/implementation-of-gaussian-naive-bayes-in-python-sklearn/)
```

* Gradient Boosting
```
Gradient Boosting is a tree method that is a variant of ensemble methods since it utilizes multiple weak models when making a prediction.  This method is considered one of the more effective predictors.  The same problems that ensemble tree algorithms encounter are true for gradient boosting.  They can often overfit, sensitive to outliers, computationally expensive, have difficulty with large datasets, and can be difficult to interpret.  Interesting enough, turning can be more difficult than random forests.  Common suggestions are to use L1 or L2 penalties and lowering the learning rates to reduce overfitting.  Reference: [Link](https://towardsdatascience.com/all-you-need-to-know-about-gradient-boosting-algorithm-part-1-regression-2520a34a502#:~:text=Gradient%20boosting%20is%20one%20of%20the%20variants%20of%20ensemble%20methods,better%20performance%20as%20a%20whole)
```

* Linear Discriminant Analysis/Learning  
```
LDA finds a linear combination of features that best separates the classes by mapping the features in lower dimensional space.  LDA is similar to PCA.  Since Logistic Regression performs poorly outside binary classification, LDA is used instead for multiple classification problems.  Reference: [Link](https://www.analyticsvidhya.com/blog/2021/08/a-brief-introduction-to-linear-discriminant-analysis/)
```

* Quadratic Discriminant Analysis/Learning
```
QDA is a more general version of LDA that uses a quadriatic decision surface instead of hyperplane to separate measurements of two or more classes.  The key assumptions is that each class follows a gausian distribution.  Reference: [Link](https://scikit-learn.sourceforge.net/0.6/auto_examples/plot_lda_vs_qda.html)
```



 