# Classification Modelling

#### Feature Selection  

`Logistic Regression`:  Large numbers of features especially categorical values can cause overfitting or irregular results.  To reduce this issue, features can be selected through L1 penalty or by using stepwise methods like forward selection or backward selection.  Scikit-learn has a exhaustive search method call `recursive feature engineering` that is a form of backward selection.  If manually creating a method then consider making the selection of a feature based on a cutoff of the `BIC` or `AIC` criteria.  

#### Feature Preparation  

`Scaling` (from Scikit-learn):  StandardScaler centers the data's mean around zero and normalizes it to have a variance of one.  QuantileTransformer(ouptut_distribution='normal') works similarly but will typically have a more normal shaped distribution.  MinMaxScaler scales the data between two points and has a minimal influence on the features.  RobustScaler reduces the importance of outliers and data that spans a larger range.  Normalizer does not normalize features but normalizes rows of data.  Scaling data is important for neural networks, regularized regression, k-nearest neighbors, support vector machines (due to gradient descent), and discriminant analysis type algorithms.  For visual demonstration of scaling, refer to this [article](https://www.kaggle.com/code/discdiver/guide-to-scaling-and-standardizing/notebook)  

`Feature Reduction`:  Using PCA is a commmon way of reducing the number of features by combining the explained variance into fewer number of principle components while not losing most of the data.  

`Feature Selection`:  Using an L1 penalty will potentially reduce the features that offer no explanatory value to coefficient of zero.  A correlation matrix showing the relation of the independent and dependent features can be used to find the pertinent features that have less than 0.2 correlation.  Using algorithmic selection can also help like using SelectKBest() and ExtraTreesClassifier() 

`Feature Improvement`: Filling missing values (**many methods), drowing NA rows, drop entire features (NA > 50%), replace NA with 0, sample balancing, removing outliers, binning  

`Feature Prep`:  Encoding, scaling, normalizing

`Visualizing`:  Seaborn's pairplot is a handy tool for determining the relationship between variables that might lead to clusters or classifications.  
#### Explaining the Classification Report

**A Quick Look at Precision, Recall, F1-score, Support, and Classes**

`Support`: Measure that is the sum of the TP and all FN values.  This means that this is the same as the actual number of examples evaluated for a class (class is of the known actual value, real outcome).  Support is more related to recall than precision ie `(Recall * Support) = TP`

`Precision`:  Evaluation describing the ratio of TP to FP.  As you get closer to one you are getting fewer FP.  A generic way of describing this metric is that of all the predictions for true, this tells you the percent that are correctly predicted.  
- of all the predicted positive cases, X % were correct.

`Recall`:  Evaluation describing the ratio of TP to FN.  As you get closer to one you are getting few FP.  A generic way of describing this metric is that of all the real outcomes of a class, how many were correctly classified.   A higher metric indicates that the model can capture a larger proportion of positive instances.  
- of all the actual positive cases, X % were correct.

`F1-score`: a type of average (harmonic mean) of `Precision` and `Recall`.  Helpful metric when the data is imbalanced.   

`Accuracy`:  Evaluation of the overall performance such that it takes `(TP + TN)/Total Records`.  This metric can be deceiving because it can predict that all cases are `TP` often in the cases of imbalanced data where one class is represented much more.  

`Macro Avg`:  unweighted mean of precision/recall/F1 calculations using all classes.  

`Weighted Avg`:  weighed mean of precision/recall/F1 calculations when considering the effect of Support as the weight.

**Bias/Variance Tradeoff** 
There is a tradeoff between how many FP and FN that are predicted.  When one is improved then the other measure typically decreases.  This means that `Precision` and `Recall` will also have this tradeoff and as we modify prediction thresholds we often see this effect.

**Evaluation of the Model**
* Prioritize classes that are most important for your goal
* Sometimes recall will be most important and othertimes precision.  In medical diagnosis you probably want to minimize false negatives.  
* Highly imbalanced data can lead to metrics not being representative.  In these cases consider:  
    * Resampling  methods
    * Different performance metrics (ROC, AUC, AUC-ROC, AUC-PR, etc)
    * Algorithmic approaches to handling imbalances (class weights, balancing, regularization)


#### Optimization  

`GridSearch`:  Searching for the right parameters is very important especially when 


#### Reference:  
https://www.analyticsvidhya.com/blog/2021/03/step-by-step-process-of-feature-engineering-for-machine-learning-algorithms-in-data-science/  