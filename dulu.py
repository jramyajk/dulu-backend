from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return send_from_directory("../frontend", "index.html")

@app.route("/sos", methods=["POST"])
def sos():
    data = request.get_json()
    print("🚨 SOS TRIGGERED:", data)
    return jsonify({"status": "sent"})
import os

if __name__ == "__main__":
port = int(os.environ.get("port",5000))
    app.run(host="0.0.0.0",port=port)