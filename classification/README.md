# Classification  

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


