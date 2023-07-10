# Smart Mobile Phone Price Prediction using Machine Learning

## intelunnati_Talented-Tyrants

## Introduction and Context

The objective of the "Smart Mobile Phone Price Prediction" project is to predict the price range of mobile phones, indicating their relative highness in terms of cost. The project utilizes machine learning algorithms and data from Kaggle.

### Price Ranges Categorization:

- 0: Low Cost (Under 10k)
- 1: Medium Cost (Between 10k-30k)
- 2: High Cost (Between 30k-50k)
- 3: Very High Cost (Above 50K)

The evaluation metric used for classification in this project is the F1 score. The F1 score can be interpreted using the following general rule of thumb:

- 0.9 - 1.0: Very Good
- 0.8 - 0.9: Good
- 0.5 - 0.8: OK
- Below 0.5: Not Good

## Model Evaluation

After multiple iterations, three machine-learning algorithms were used to predict mobile phone prices. The F1 scores achieved by each algorithm are as follows:

- KNearestNeighbors: 0.93
- DecisionTreeClassifier: 0.81
- RandomForestClassifier: 0.86

Based on these results, the KNearestNeighbors model emerged as the top performer with the highest F1 score of 0.93.

## Model Deployment

The trained model was converted into a pickle file. Pickle allows us to serialize machine learning models in their existing state, making it possible to reuse them when needed.

For deployment, the Streamlit framework was used to create a website where users can interact with the model and predict the price range of their mobile phones.

You can access the deployed website [here](https://intelunnatitalented-tyrants-16sdw5yqmay.streamlit.app/).
## Demo Vedio
[![Video Title](http://img.youtube.com/vi/JfAcF1QUxX0/0.jpg)](https://www.youtube.com/watch?v=jvbkvwVc6Tw "Video Title")





