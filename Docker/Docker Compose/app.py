from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    hostname = socket.gethostname()
    return f"Hello from {hostname}"

if __name__ == "__main__":
    # Listen on all interfaces so Docker can route traffic in
    app.run(host="0.0.0.0", port=5000)