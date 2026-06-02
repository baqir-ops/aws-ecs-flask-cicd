from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "CI/CD Deployment Successful!",
        "status": "success",
        "environment": os.getenv("APP_ENV", "development")
    }

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
