from flask import Flask, jsonify
import requests

app = Flask(__name__)
API_KEY = "enter"

@app.route("/token/<mint>")
def get_token(mint):
    url = f"https://public-api.birdeye.so/defi/token/latest-info/{mint}"
    headers = {"x-api-key": API_KEY}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json().get("data", {})
        token_info = {
            "name": data.get("name", "Unknown"),
            "symbol": data.get("symbol", "???"),
            "address": mint
        }
        return jsonify(token_info), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return {"status": "Birdeye proxy is running."}
