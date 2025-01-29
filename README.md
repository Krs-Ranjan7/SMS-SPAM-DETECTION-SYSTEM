SMS Spam Detection
Overview
The SMS Spam Detection project uses a machine learning model to predict if an SMS is spam or not. It's developed in Python and deployed with Streamlit.

Technology Used
Python

Scikit-learn

Pandas

NumPy

Streamlit

Features
Data collection and preprocessing

Exploratory Data Analysis (EDA)

Model building and selection

Web deployment using Streamlit

Data Collection
The dataset contains over 5,500 SMS messages, categorized as spam or not spam, sourced from Kaggle. [Access the dataset here](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

Data Cleaning and Preprocessing
The dataset was cleaned to handle null values and duplicates, and label-encoded for the "type" column. Text preprocessing involved tokenization, removing special characters, stop words, punctuation, stemming, and converting text to lowercase.

Exploratory Data Analysis
EDA was conducted to understand the dataset better. Character, word, and sentence counts were calculated. Correlations and various visualizations, such as bar charts, pie charts, summaries, heatmaps, and word clouds, were created.

Model Building and Selection
Multiple classifiers were evaluated, including Naive Bayes, random forest, KNN, decision tree, logistic regression, ExtraTreesClassifier, and SVC. The model with the highest precision was selected, achieving 100% precision.

Web Deployment
The model is deployed on the web using Streamlit. Users can input a message to see if it is spam or not.

Demo
Experience the SMS Spam Detection model [here](https://ranjan-sms-spam-detection-system.streamlit.app/)
