# PythonGradesPrediction

Welcome to the PythonGradesPrediction project, an innovative machine learning initiative designed to revolutionize the way we interpret and predict the sentiment and grading of reviews. Leveraging the power of Python, this project aims to accurately predict not only if the opinions expressed in a review are positive or negative but also to estimate the precise grading of the reviews on a scale from 1 to 5 stars.

## Project Overview

The PythonGradesPrediction project is structured around the application of cutting-edge machine learning techniques to analyze review text data. The project's primary objectives are:

1. **Sentiment Analysis**: To determine the sentiment of a review, categorizing it as either positive or negative.
2. **Grade Prediction**: To predict the exact grade (from 1 to 5 stars) of the review, based on the textual content and sentiment analysis.

## Technology Stack

The project is implemented in Python, utilizing several libraries and frameworks pivotal in the field of machine learning and natural language processing (NLP). The core of the project revolves around experimenting with and evaluating the performance of three different machine learning models:

- **MultinomialNB**: A Naive Bayes classifier that is well-suited for classification with discrete features (e.g., word counts for text classification).
- **KNN (K-Nearest Neighbors)**: A simple, instance-based learning algorithm used for classification and regression.
- **CountVectorizer**: Used in conjunction with machine learning models to convert a collection of text documents to a matrix of token counts, facilitating the analysis and prediction processes.

## Getting Started

To begin working with the PythonGradesPrediction project, please ensure you have Python installed on your machine. Then, follow these steps to set up your environment:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the main project script to start experimenting with sentiment analysis and grade predictions.

## Models Evaluation

Each of the three models mentioned above has been rigorously tested on a dataset of reviews to evaluate their performance in both sentiment analysis and grade prediction tasks. The evaluation process involved comparing the accuracy, precision, recall, and F1 scores of each model to identify the most effective approach for our objectives.

## Conclusion and Future Work

This project was a small study project during our last year of study at OUT of Nantes

## License

This project is licensed under the MIT License - see the LICENSE file for details.
