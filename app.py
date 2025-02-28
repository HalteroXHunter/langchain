from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Import the ice_break_with function from the test_ice_breaker module
from test_ice_breaker import ice_break_with

# Initialize the Flask application
app = Flask(__name__)


# Define the route for the home page
@app.route("/")
def index():
    # Render the index.html template
    return render_template("index.html")


# Define the route for processing the form submission
@app.route("/process", methods=["POST"])
def process():
    # Get the name from the form submission
    name = request.form["name"]

    # Call the ice_break_with function to get the summary, facts, interests, ice breakers, and profile picture URL
    summary_and_facts, interests, ice_breakers, profile_pic_url = ice_break_with(
        name=name
    )

    # Return the results as a JSON response
    return jsonify(
        {
            "summary_and_facts": summary_and_facts.to_dict(),
            "interests": interests.to_dict(),
            "ice_breakers": ice_breakers.to_dict(),
            "picture_url": profile_pic_url,
        }
    )


# Run the Flask application
if __name__ == "__main__":
    # Start the Flask development server
    app.run(host="0.0.0.0", debug=True)
