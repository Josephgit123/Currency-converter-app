import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "YOUR_EXCHANGE_RATE_API_KEY"
BASE_URL = "https://v6.exchangerate-api.com/v6"

@app.route("/", methods=["GET", "POST"])
def home():
    conversion = None
    if request.method == "POST":
        amount = float(request.form.get("amount"))
        from_currency = request.form.get("from_currency")
        to_currency = request.form.get("to_currency")

        response = requests.get(f"{BASE_URL}/{API_KEY}/pair/{from_currency}/{to_currency}")
        if response.status_code == 200:
            rate = response.json()["conversion_rate"]
            conversion = round(amount * rate, 2)
        else:
       
