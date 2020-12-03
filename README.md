# Setimental-Analyzer

The file basic-analyzer has the source code to train as well as run a sentiment detection algorithm, the above uses bag of word algorithm to parse the input data as a vector and different machine learning algorithms, such as:
+ Support Vector Machine
+ Logistic Regression
+ Guassian Naive Bayes
+ Decision Tree

These algorithms are imported from sklearn library of python.
I have also evaluated error and accuracy of the model on some of the standard sklearn functions:
+ F1 score
+ Mean squared error
+ ML model score (i.e. the predefined model score funstion of different machine learning algorithm)

I have used only 10000 data elements to train the model and it provides an accuracy of around 70% for various model. Details can be seen in Jupyter Notebook.

# System 
The system judges and categorises the input text data into three broad categories as:
+ Positive
+ Negative
+ Neutral

The user can provide any type of text input and it can be categorised into these broad categories, the system can be manipulated with different dataset which provide more sentimental data and and can be used to categorise other specific and deep emotions.
# Dataset
The Amazon product review dataset was used as the basis and it was shortened, otherwise it would require a lot of computational power to train a model on all  50 Million data elements. The data is parsed in JSON format so it easily accessible and provides a lot of meta-data, which man be used to manipualte the system as per the system design and need of developers.
https://jmcauley.ucsd.edu/data/amazon/

The file to slice the data set as per the need is slice.py, it can modified as per need.
