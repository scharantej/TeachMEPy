
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app
app = Flask(__name__)

# Define the root route
@app.route("/")
def index():
    """
    Renders the index page.
    """
    return render_template("index.html")

# Define the lessons route
@app.route("/lessons")
def lessons():
    """
    Renders the lessons page.
    """
    return render_template("lessons.html")

# Define the quiz route
@app.route("/quiz")
def quiz():
    """
    Renders the quiz page.
    """
    return render_template("quiz.html")

# Define the results route
@app.route("/results", methods=["POST"])
def results():
    """
    Renders the results page.
    """
    score = 0
    
    # Get the user's answers
    answers = request.form.getlist("answer")
    
    # Check the user's answers
    for answer in answers:
        if answer == "correct":
            score += 1
    
    # Render the results page
    return render_template("results.html", score=score)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
