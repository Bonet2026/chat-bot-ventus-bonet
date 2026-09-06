from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Chat Bot Ventus-Bonet activo"

@app.route("/webhook", methods=["GET"])
def verify():
    return "WEBHOOK OK"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print(data)
    return "EVENT_RECEIVED", 200
