# Regression Modelling 

#### Feature Selection  

`Remove Features that are Highly Correlated with Other Features` - features with correlations over 0.8 are very similar and the extra featues will not help in fitting the model so only one of the features can be left in the model or consider combining the features becasue their combination might have more explanatory power.  

`Check that features are balanced and somewhat normally distributed` - considered transforming the data to make the features not skewed.

`Check that features plotted versus the target are linear` - consider transforming the feature to create a linear relationship so it can be modelled effectively

`Check that features are correlated with the target` - if there is no correlation then the feature can be removed.  Another way of doing this is to run a lasso regression with an optimized C parameter.  

`If many features are correlated over 0.3 then reduce feature space by running PCA` - this will map the significant features into a lower dimensional space  

`If a penalty term is used then ensure that the data is previously scaled` - most likely the algorithm uses a penalty term with gradient descent so the variables must have a similar range to be equally weighted.

`Weight the parameters differently` - ensures that the feature is included in the model.  

`Remove outliers` - distortions in the data are not always generalized well.  Removing these values during preprocessing can improve the model.  

`Use k-fold cross validation` - this will help determine if your model is generalized or overfitting.  

`Vary the algorithms` - the relationship might not be linear so using more complex algorithms like support vector regression or decision tree algorithms.  

`Model Interactive terms` - For two continuous variables, create an interaction term by multiplying the two variables together. For example, if you have variables X1 and X2, the interaction term would be X1 * X2. If you're dealing with categorical variables, create dummy variables for the interaction effect and then multiply them as appropriate.  Add the interactive term into the model and then evaluate if the interactive term is significant (t-test, p value).  These terms can cause overfitting so make sure to use cross validation when evaluating model generalization.  Also consider creating a Partial Dependence Plots (PDP) and identifying tree models that split based on more than one condition.  