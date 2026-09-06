from flask import Flask, request
import os

app = Flask(__name__)

VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "ventus_bonet_webhook_2026")


@app.route("/", methods=["GET"])
def home():
    return "Chat Bot Ventus-Bonet activo"


@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200

    return "Forbidden", 403


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True)

    print("WEBHOOK RECIBIDO:")
    print(data)

    return "EVENT_RECEIVED", 200
