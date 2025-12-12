import os
from flask import Flask, jsonify

app = Flask(__name__)
port = int(os.environ.get("PORT", 80))


@app.route("/users/")
def home():
    users = [
        {"id": 1, "username": "karl"},
        {"id": 2, "username": "basti"},
        {"id": 3, "username": "jaki"},
    ]

    return users


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)
