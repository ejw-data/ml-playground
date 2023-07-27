# ML Algorithms for Data Mining  
This list is comprised only of stochastic methods of data mining but there are more deterministic methods that use algorithms such as routing algorithms and sequence algorithms.  

## Predictive  
These types of models are trained with known outcomes (supervised) thus allowing the models to be evaluated for the quality of their prediction.  

### Regression
* OLS
* Ridge
* Lasso
* ElasticNet
* Polynomial
* Tree Regressor
* Stochastic Gradient Descent Regressor
* Support Vector Regressor (kernel='linear')
* Support Vector Regressor (kernel='rbf')
* EnsembleRegressors

### Classification
* Logistic (not regularized)
* Logistic (regularized)
* Tree Classifier
* Random Forests
* Stochastic Gradient Descent
* Kernel Approximation
* K-Nearest Neighbors
* Support Vector Classifiers
* Ensemble Classifiers
* Naive Bayes (Text)


## Descriptive  
These types of models typically do not have known outcomes (unsupervised) so the relations generated a based upon grouping similarities in the features.  

### Clustering  [Link](https://www.freecodecamp.org/news/8-clustering-algorithms-in-machine-learning-that-all-data-scientists-should-know/)
* Centroid/Spacial - uses a distance metric to evaluate membership.  
    * KMeans
    * Mini-Batch KMeans
    * Affinity Propogation  
        * does not need the number of clusters defined initially
* Density
    * DBSCAN
    * OPTICS - find meaningful clusters in data that varies in density. It does this by ordering the data points so that the closest points are neighbors in the ordering
* Hierarchical - reductive method where branches are merged based on proximity
    * Balance Iterative Reducing and Clustering using Hierarchies (BIRCH)
        * does not need the number of clusters defined initially
    * Mean-Shift
        * does not need the number of clusters defined initially
        * does not scale well to large datasets
    * Agglomerative Hierarchy
        * Good at finding small clusters
        * Visualization looks like dendrogram
    * Divisive Hierarchical
* Soft - object can belong to multiple clusters and each data point has a probability of existing in each cluster
    * Fuzzy Clustering - 
    * Gaussian Mixture Model
* Graph 
    * Spectral Clustering
* Distribution-based
    * Gaussian - points further from center have a lower membership probability  
* Subspace - form of feature selection
    * Top-down (projection-based) - project data onto subspaces and clustering the lower dimensional data
    * Bottom-up - finds dense regions in low-dimensional space (using density-based clustering) and combines the regions to form clusters in full-dimensional space.  

### Association Rule  
* similarity
* text similarity
* basket of goods
* collaborative filtering
* content-based
* demographic
* hybrid
* knowledge-based
* utility-based

### Dimensionality Reduction
* Descriment Analysis
    * PCA
    * MCA
    * ICA
    * LDA - latent dirichlet allocation
    * Factor Analysis
* Kernel Approximation
* Isomap/Sprectral Embedding
* LLE


### Deterministic Modeling
* Discrete Event Simulations
* Agent-based Simulation
* Continuous Simulations
* Heuristic Algorithms
* Meta-heuristic Algorithms
* Queueing Algorithms
* Sequencing Algorithms
* Scheduling/Dispatching Algorithms
* Linear Programming
* Mixed Integer Linear Programming
* Dynamic Programming

* Genetic Algorithms
* Neuro Evolutionary Augmented Topologies  
* Computer Vision
* Natural Language Processing
* Reinforcement Learning
* Time Series  
* Recommendation Engine??  
* Neural Networks


### Algorithms by Purpose
* Anomaly detection



Notes:
Subspace, Lasso, and Random Forests can be used for feature selection

