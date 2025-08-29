from flask import Flask, render_template, request, jsonify, session
import requests
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key"

API_KEY = "589bfca80fd94a301bc0a4ad"  
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    base_currency = data.get("base_currency")
    target_currency = data.get("target_currency")
    amount = float(data.get("amount"))

    response = requests.get(API_URL + base_currency)
    rates = response.json().get("conversion_rates", {})

    if target_currency in rates:
        converted_amount = amount * rates[target_currency]

    
        if "history" not in session:
            session["history"] = []
        session["history"].append({
            "base": base_currency,
            "target": target_currency,
            "amount": amount,
            "converted": converted_amount,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        session.modified = True

        return jsonify({"converted_amount": converted_amount})
    else:
        return jsonify({"error": "Invalid currency"}), 400

@app.route("/history")
def history():
    return jsonify(session.get("history", []))

if __name__ == "__main__":
    app.run(debug=True)
