from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def receive_data():
    data = request.json
    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    sheet_url = "https://script.google.com/macros/s/AKfycbwQiuDcdFWMix9Qs4ol4twfUoGviI7gF3YwHHozv0wqSbZT71VrsSz9T-Af6ijwM6yXTw/exec"
    response = requests.post(sheet_url, json=data)

    return jsonify({"status": "ok", "gs_response": response.text}), response.status_code

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # берем порт из окружения
    app.run(host="0.0.0.0", port=port)
