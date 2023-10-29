# Import necessary libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier

# Initialize the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Sample dataset (replace with your own dataset)
documents = [
    "I love this product!",
    "Terrible experience, would not recommend.",
    "The movie was great.",
    "Awful customer service.",
    "It's a fantastic book.",
]

# Corresponding labels for sentiment analysis
labels = ["positive", "negative", "positive", "negative", "positive"]

# Convert the documents into TF-IDF features
X = tfidf_vectorizer.fit_transform(documents)

# Initialize the decision tree classifier
decision_tree = DecisionTreeClassifier()

# Train the decision tree model
decision_tree.fit(X, labels)

# Function to predict sentiment based on user input
def predict_sentiment(user_input):
    input_features = tfidf_vectorizer.transform([user_input])
    prediction = decision_tree.predict(input_features)
    return prediction[0]

# Simple chatbot loop
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        break
    
    # Predict sentiment based on user input
    sentiment = predict_sentiment(user_input)
    
    if sentiment == "positive":
        response = "Bot: That sounds great!"
    else:
        response = "Bot: I'm sorry to hear that."
    
    print(response)

