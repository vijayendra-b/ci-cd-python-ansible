from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"CI/CD Pipeline with Jenkins and Ansible | Time: {timestamp}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
