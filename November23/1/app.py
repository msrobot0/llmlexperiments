import spacy
from flask import Flask, render_template, request, jsonify

# Load the spaCy model with word embeddings
nlp = spacy.load("en_core_web_md")

# Initialize a Flask app
app = Flask(__name__)

# Create a route for the homepage
@app.route("/")
def index():
    return render_template("index.html")

# Create a route for processing text categorization
@app.route("/categorize", methods=["POST"])
def categorize():
    text = request.form.get("text")

    # Process the input text with spaCy
    doc = nlp(text)

    # Implement your text categorization logic here
    # For this example, we'll use a simple rule to classify text as "Positive" or "Negative"
    if "happy" in text.lower():
        category = "Positive"
    else:
        category = "Negative"

    return jsonify({"category": category})

if __name__ == "__main__":
    app.run(debug=True)

