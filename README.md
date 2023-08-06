# ml-playground  

Author:  Erin James Wills, ejw.data@gmail.com  

![Machine Learning Playground](./images/ml-playground.png)  
<cite>Photo by <a href="https://unsplash.com/@jontyson?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jon Tyson</a> on <a href="https://unsplash.com/s/photos/playground?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></cite>
<br>

## Overview  
<hr>  
Testing the limitations, inabilities, and strengths of models with synthetic data  

<br>

## Content  
* Classification
    * Gaussian Naive Bayes (continuous data)
    * Naive Bayes (text)
    * Gradient Boosting
    * Linear Discriminant Learning
    * Quadratic Discriminant Learning
    * Logistic
    * KNN
    * Decision Trees
    * Random Forest
    * Isolation Forest - identifies early terminating branches as outliers
    * Support Vector Classifier  
<br>

* Clustering
    * Centroid/Distance
        * KMeans
    * Density
        * DBSCAN
    * Hierarchical
        * Agglomerative Hierarchy
        * Divisive Hierarchical
    * Gaussian Mixture Models (GMM)
    * Mean Shift
    * Affinity Propogation
    * Fuzzy C-Means (*in-progress)
    * Balanced Iterative Reducing and Clustering using Hierarchies (BIRCH)
    * Self-Organizing Maps (SOM)
    * Ordering Points to Identify the Clustering Structure (OPTICS)
    * Spectral  

<br>

* Computer Vision (future)

<br>

* Natural Language Processing 
    * Keyword Extraction
    * Lemmazation
    * Named Entity Recognition
    * Named Recognition
    * Sentiment
    * Stemming
    * String Matching
    * Summarization
    * Text Classification
    * Topic Modelling  
<br>

* Neural Networks
    * Classification Binary
    * Classification KMeans
    * Classification Binary Backpropogation (*in-progress)
    * Classification Multiclass
    * Clustering Self Organizing Maps (*in-progress)
    * Genetic Neural Networks (*in-progress)
    * Neural Structured Learning
    * Multiregression (linear)
    * NeuroEvolution Augmenting Topologies (*in-progress)
    * Regression (linear)
    * Regression (non-linear)  

<br>

* Recommendation Engines - [Link](https://medium.com/mlearning-ai/recommendation-systems-arl-association-rule-learning-bed1a07b5d9a#:~:text=Simple%20Recommender%20Systems%3A%20Makes%20general,based%20on%20similarities%20of%20products.)
    * Simple Recommendation Systems - uses business knowledge/heuristics or simple sequencing
        * Utility-based - rules based on simple filters
        * Knowledge-based - rules based on user input that is used as a filter
    * Association Rule Learning - uses rules learned through recurrances in a dataset  
        * Basket of Good Random Forest - uses random forests to group products together
        * Basket of Goods Association Rule - uses apriori and association to generate relations
    * Content-Based Filtering - uses similarities to group items and assume the same outcome
        * Text Similarity (CountVectorizer) - uses a text corpus and converts to vector such that similar vectors are related
        * Content-based - uses product similarity to suggest similar options
        * Content-based2 - same as above
    * Collaborative Filtering (User, Product, or Model-based) - uses common relationships beteen users and products
        * Demographic-based - uses trends in demographics to create a rule
        * Collaborative Filtering (*in-progress)
    * Ensemble - uses multiple techniques
        * Hybrid (*in-progress) - uses content-based and collaborative filtering  

<br>

* Regression
    * Feature Transformation (*in-progress) 
    * Time Lag of Feature - incorporates a time dependent feature into the model
    * Change Over Time - incorporates the difference between consecutive datapoints
    * Lowess and Loess Smoothing - non-parametric smoothing
    * Ordinary Least Squares - typically non-regularized method that minimizes the sum of the squared errors
    * Lasso - regularization method that shrinks the coefficients to even zero (l1 regularization)
    * Ridge - regularization method that minimizes the model complexity (especially multicollinearity) but doesn't shrink the coeffients to zero (l2 regularization)
    * ElasticNet - regularization method that uses l1 and l2 regularization
    * Polynomial - transform features then applies the ordinary least squares regression
    * Support Vector Regression
    * Quantile Regression 

<br>

* Reinforcement Learning (future)  

<br>

* Time Series
    * Survival Analysis - expected duration of time until an event occurs
    * Time Series Decomposition - separating cyclic events from trends

<br>

## Technologies    
*  Python

<br>

## Libraries
* Lifelines
* statsmodels.tsa
* neat
* yake
* nltk
* spacy
* difflib
* transformers
* scikit-learn
* tensorflow
* keras
* minisom
* deap
* neural_structured_learning
* mlxtend
* scikit-surprise
* gym

<br>

## Data Source  
Datasets were generated through scikit-learn data generators or simple algorithms

<br>

## Setup and Installation  
1. Environment needs the following:  
    *  Python 3.6+   
    *  scikit-learn
1. Activate your environment
1. Clone the repo to your local machine
1. Navigate the terminal to the repo folder
1. In the terminal, run any of the Jupyter Notebooks  

<br>

## References
- https://www.machinelearningplus.com/time-series/time-series-analysis-python/ 
- https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/

