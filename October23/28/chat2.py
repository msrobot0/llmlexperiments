# Import necessary libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

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

# Initialize the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Convert the documents into TF-IDF features
X = tfidf_vectorizer.fit_transform(documents)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Initialize the decision tree classifier
decision_tree = DecisionTreeClassifier()

# Train the decision tree model
decision_tree.fit(X_train, y_train)

# Make predictions on the test data
predictions = decision_tree.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

print("Accuracy:", accuracy)
print("Classification Report:\n", report)

