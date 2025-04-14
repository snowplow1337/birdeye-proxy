from flask import Flask, jsonify
import requests

app = Flask(__name__)
API_KEY = "d9e23c8f480f4c2a871cfcdfd228f9b0"

@app.route("/token/<mint>")
def get_token(mint):
    url = f"https://public-api.birdeye.so/public/token/{mint}"
    headers = {"x-api-key": API_KEY}
    try:
        response = requests.get(url, headers=headers)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return {"status": "Birdeye proxy running!"}
