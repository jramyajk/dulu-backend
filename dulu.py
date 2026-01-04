from flask import Flask, request, jsonify, send_from_directory
import os

BASE_DIR = os.path.dirname(os.path.abspath(_file_))
FRONTEND_DIR = os.path.join(BASE_DIR, "../frontend")

app = Flask(_name_, static_folder=FRONTEND_DIR, template_folder=FRONTEND_DIR)

@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/sos", methods=["POST"])
def sos():
    data = request.get_json()
    print("🚨 SOS TRIGGERED:", data)
    return jsonify({"status": "sent"})

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)