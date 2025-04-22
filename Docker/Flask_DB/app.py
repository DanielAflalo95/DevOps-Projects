# app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)

# Read runtime env‑vars (you’ll fill these in later via --env-file or -e)
PORT    = int(os.getenv("PORT",     5000))
MESSAGE = os.getenv("MESSAGE",      "Hello from Flask in Docker!")
DB_HOST = os.getenv("DB_HOST",      "localhost")
DB_PORT = os.getenv("DB_PORT",      "5432")

@app.route("/")
def index():
    return jsonify({
        "message": MESSAGE,
        "database": {
            "host": DB_HOST,
            "port": DB_PORT
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
