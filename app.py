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
        "Content-Type": "application/json",
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


def menu_principal():
    return (
        "👋 ¡Hola! Bienvenido a *VENTUS – BONET CONTRATISTAS GENERALES*.\n\n"
        "¿Qué información deseas conocer?\n\n"
        "1️⃣ Departamentos disponibles\n"
        "2️⃣ Precios y formas de pago\n"
        "3️⃣ Planos y distribución\n"
        "4️⃣ Ubicación\n"
        "5️⃣ Características del edificio\n"
        "6️⃣ Alquiler temporal / Airbnb\n"
        "7️⃣ Hablar con un asesor\n\n"
        "👉 Responde con el número de la opción que deseas."
    )


def respuesta_opcion(opcion):
    if opcion == "1":
        return (
            "🏢 *DEPARTAMENTOS DISPONIBLES*\n\n"
            "En VENTUS contamos con departamentos diseñados "
            "para vivir o para alquiler temporal.\n\n"
            "Si deseas conocer las unidades disponibles, "
            "escribe *ASESOR* y te ayudaremos con la información actualizada."
        )

    elif opcion == "2":
        return (
            "💰 *PRECIOS Y FORMAS DE PAGO*\n\n"
            "Te podemos brindar información sobre precios, "
            "separación y formas de pago disponibles.\n\n"
            "Para recibir la información actualizada, "
            "escribe *ASESOR*."
        )

    elif opcion == "3":
        return (
            "📐 *PLANOS Y DISTRIBUCIÓN*\n\n"
            "VENTUS cuenta con una distribución moderna y funcional.\n\n"
            "Podemos enviarte información sobre los planos "
            "y distribución de los departamentos.\n\n"
            "Escribe *PLANOS* para continuar."
        )

    elif opcion == "4":
        return (
            "📍 *UBICACIÓN*\n\n"
            "VENTUS está ubicado en Wanchaq – Cusco.\n\n"
            "Es una zona con acceso a servicios, comercios "
            "y vías de conexión con diferentes puntos de la ciudad.\n\n"
            "Escribe *UBICACIÓN* si deseas recibir más información."
        )

    elif opcion == "5":
        return (
            "🏗️ *CARACTERÍSTICAS DEL EDIFICIO*\n\n"
            "VENTUS ha sido proyectado pensando en comodidad, "
            "funcionalidad y una imagen moderna.\n\n"
            "Podemos brindarte información sobre acabados, "
            "áreas y características de los departamentos.\n\n"
            "Escribe *CARACTERÍSTICAS* para continuar."
        )

    elif opcion == "6":
        return (
            "🏠 *ALQUILER TEMPORAL / AIRBNB*\n\n"
            "Los departamentos de VENTUS también están pensados "
            "para poder utilizarse como unidades de alquiler temporal.\n\n"
            "Esto representa una alternativa interesante para quienes "
            "buscan una propiedad con potencial de uso para Airbnb.\n\n"
            "Escribe *AIRBNB* para recibir más información."
        )

    elif opcion == "7":
        return (
            "👨‍💼 *ASESOR COMERCIAL*\n\n"
            "Perfecto. Un asesor de BONET puede ayudarte con información "
            "sobre disponibilidad, precios, planos y proceso de compra.\n\n"
            "📲 Déjanos tu consulta y continuamos contigo."
        )

    else:
        return menu_principal()


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

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
                incoming_text = message["text"]["body"].strip()
                incoming_lower = incoming_text.lower()

                print("MENSAJE:", incoming_text)
                print("REMITENTE:", sender)

                if incoming_lower in [
                    "hola",
                    "hola!",
                    "buenas",
                    "buenos dias",
                    "buenos días",
                    "buenas tardes",
                    "buenas noches",
                    "menu",
                    "menú",
                    "inicio"
                ]:
                    reply = menu_principal()

                elif incoming_text in [
                    "1", "2", "3", "4", "5", "6", "7"
                ]:
                    reply = respuesta_opcion(incoming_text)

                elif incoming_lower in [
                    "asesor",
                    "asesora",
                    "vendedor",
                    "ventas"
                ]:
                    reply = respuesta_opcion("7")

                else:
                    reply = (
                        "Gracias por escribirnos. 😊\n\n"
                        "Para ayudarte mejor, selecciona una opción:\n\n"
                        "1️⃣ Departamentos disponibles\n"
                        "2️⃣ Precios y formas de pago\n"
                        "3️⃣ Planos y distribución\n"
                        "4️⃣ Ubicación\n"
                        "5️⃣ Características del edificio\n"
                        "6️⃣ Alquiler temporal / Airbnb\n"
                        "7️⃣ Hablar con un asesor"
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
