# app.py
from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

@app.route('/')
def home():
    """Root endpoint returning a welcome message."""
    return "Welcome to the Flask App!"

@app.route('/greet', methods=['GET'])
def greet():
    """
    Example endpoint: /greet?name=John
    Returns a greeting message in JSON format.
    """
    name = request.args.get('name', '').strip()

    # Input validation
    if not name:
        return jsonify({"error": "Missing 'name' query parameter"}), 400

    return jsonify({"message": f"Hello, {name}!"})

@app.errorhandler(404)
def not_found(error):
    """Custom 404 error handler."""
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def server_error(error):
    """Custom 500 error handler."""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True)
