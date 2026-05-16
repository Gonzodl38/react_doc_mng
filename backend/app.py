from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def home():
    return "HOME WORKING"


@app.route("/api/test")
def api_test():
    return {"message": "Backend working"}

CORS(app)

@app.route("/api/test")
def test():
    return {"message": "Backend working"}

if __name__ == "__main__":
    app.run(debug=True)