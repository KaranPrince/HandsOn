from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask app!"

if __name__ == "__main__":
    # listen on 0.0.0.0 so container ports work
    app.run(host="0.0.0.0", port=5000)
