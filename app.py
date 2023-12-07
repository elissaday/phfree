from flask import Flask, render_template

# Initialize a Flask application
app = Flask(__name__, static_url_path="/static")

# Route for the home page ("/") with support for GET and POST requests
@app.route("/", methods=["GET", "POST"])
def home():
    # Render the homepage.html template when accessing the home route
    return render_template("homepage.html")

# Route for the team page ("/team")
@app.route("/team")
def team():
    # Render the team.html template when accessing the team route
    return render_template("team.html")

# Route for the about page ("/about")
@app.route("/about")
def about():
    # Render the about.html template when accessing the about route
    return render_template("about.html")

# Route for the contact page ("/contact") with support for GET and POST requests
@app.route("/contact", methods=["GET", "POST"])
def contact():
    # Render the contact.html template when accessing the contact route
    return render_template("contact.html")

# Run the app only if this script is executed directly (not imported)
if __name__ == "__main__":
    # Run the app in debug mode for easier debugging
    app.run(debug=True)
