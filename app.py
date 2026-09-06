from flask import Flask, request
import os
import requests

app = Flask(__name__)

VERIFY_TOKEN = os.environ.get(
    "VERIFY_TOKEN",
    "ventus_bonet_webhook_2026"
)

WHATSAPP_TOKEN = os.environ.get("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.environ.get("PHONE_NUMBER_ID")


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


def send_whatsapp_message(to, text):
    url = f"https://graph.facebook.com/v25.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "body": text
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=20
    )

    print("RESPUESTA WHATSAPP:", response.status_code)
    print(response.text)


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True)

    print("WEBHOOK RECIBIDO:")
    print(data)

    try:
        entry = data["entry"][0]
        changes = entry["changes"][0]
        value = changes["value"]

        messages = value.get("messages", [])

        if messages:
            message = messages[0]

            sender = message.get("from")
            message_type = message.get("type")

            if message_type == "text":
                incoming_text = message["text"]["body"]

                print("MENSAJE:", incoming_text)
                print("REMITENTE:", sender)

                reply = (
                    "¡Hola! 👋 Soy el asistente virtual de "
                    "VENTUS - BONET CONTRATISTAS GENERALES.\n\n"
                    "Gracias por comunicarte con nosotros. "
                    "¿En qué podemos ayudarte?"
                )

                send_whatsapp_message(sender, reply)

    except Exception as e:
        print("ERROR:", e)

    return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
