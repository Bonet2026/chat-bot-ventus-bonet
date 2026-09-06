from flask import Flask, request
import os
import requests

app = Flask(__name__)

# ==============================
# CONFIGURACIÓN
# ==============================

VERIFY_TOKEN = os.environ.get(
    "VERIFY_TOKEN",
    "ventus_bonet_webhook_2026"
)

WHATSAPP_TOKEN = os.environ.get("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.environ.get("PHONE_NUMBER_ID")


# ==============================
# ENVIAR MENSAJE POR WHATSAPP
# ==============================

def send_whatsapp_message(to, text):

    url = f"https://graph.facebook.com/v26.0/{PHONE_NUMBER_ID}/messages"

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


# ==============================
# MENÚ PRINCIPAL
# ==============================

def menu_principal():

    return (
        "¡Hola! 👋 Bienvenido a VENTUS - BONET CONTRATISTAS GENERALES.\n\n"

        "🏢 *VENTUS | Wanchaq - Cusco*\n\n"

        "Estoy aquí para ayudarte a conocer nuestro proyecto.\n\n"

        "Elige una opción:\n\n"

        "1️⃣ Conocer VENTUS\n"
        "2️⃣ Ver departamentos disponibles\n"
        "3️⃣ Información de los departamentos 501 y 502\n"
        "4️⃣ VENTUS para Airbnb / alquiler temporal\n"
        "5️⃣ Ubicación del proyecto\n"
        "6️⃣ Hablar con un asesor\n\n"

        "👉 Responde con el número de la opción que deseas."
    )


# ==============================
# RESPUESTAS
# ==============================

def responder(texto):

    texto = texto.lower().strip()

    # SALUDO
    if texto in [
        "hola",
        "ola",
        "buenas",
        "buenos dias",
        "buenas tardes",
        "buenas noches",
        "inicio",
        "menu",
        "menú"
    ]:
        return menu_principal()


    # OPCIÓN 1
    if texto in ["1", "ventus", "proyecto", "informacion", "información"]:

        return (
            "🏢 *VENTUS - BONET CONTRATISTAS GENERALES*\n\n"

            "Un proyecto multifamiliar ubicado en Wanchaq, Cusco, "
            "pensado para quienes buscan una vivienda moderna "
            "y también una alternativa para alquiler temporal.\n\n"

            "✨ Características destacadas:\n"
            "• Departamentos modernos\n"
            "• Diseño funcional\n"
            "• Ubicación estratégica en Wanchaq\n"
            "• Espacios pensados para vivienda y alquiler temporal\n"
            "• Departamentos 501 y 502 con aires de uso exclusivo\n\n"

            "Escribe *2* para conocer los departamentos disponibles."
        )


    # OPCIÓN 2
    if texto in ["2", "departamentos", "departamento", "disponibles"]:

        return (
            "🏠 *DEPARTAMENTOS VENTUS*\n\n"

            "Tenemos diferentes alternativas dentro del proyecto "
            "VENTUS, de acuerdo con tus necesidades.\n\n"

            "⭐ También contamos con los departamentos *501 y 502*, "
            "que incluyen sus aires/azotea de uso exclusivo.\n\n"

            "👉 Escribe *3* para conocer específicamente los "
            "departamentos 501 y 502.\n\n"

            "👉 Escribe *6* si deseas que un asesor te contacte."
        )


    # OPCIÓN 3
    if texto in [
        "3",
        "501",
        "502",
        "departamento 501",
        "departamento 502",
        "aires"
    ]:

        return (
            "⭐ *DEPARTAMENTOS 501 Y 502*\n\n"

            "Los departamentos 501 y 502 tienen una característica "
            "especial: incluyen sus *aires/azotea de uso exclusivo*.\n\n"

            "🏠 En estos aires se contempla además una "
            "*habitación adicional*, ampliando las posibilidades "
            "de uso del departamento.\n\n"

            "Esto permite aprovechar mejor el espacio y generar "
            "un ambiente adicional para dormitorio, huéspedes, "
            "oficina u otros usos según el diseño final.\n\n"

            "📲 Si deseas conocer la distribución y características "
            "con mayor detalle, escribe *6* para hablar con un asesor."
        )


    # OPCIÓN 4
    if texto in [
        "4",
        "airbnb",
        "alquiler",
        "alquiler temporal",
        "inversion",
        "inversión"
    ]:

        return (
            "🏡 *VENTUS + ALQUILER TEMPORAL*\n\n"

            "VENTUS también está pensado para quienes desean "
            "utilizar su departamento como una unidad para "
            "alquiler temporal tipo Airbnb.\n\n"

            "Esto convierte al proyecto en una alternativa interesante "
            "tanto para vivienda como para uso de alquiler temporal.\n\n"

            "📌 No te damos una rentabilidad estimada sin datos reales; "
            "nuestro objetivo es mostrarte el potencial del inmueble.\n\n"

            "👉 Escribe *6* para conversar con un asesor."
        )


    # OPCIÓN 5
    if texto in [
        "5",
        "ubicacion",
        "ubicación",
        "donde",
        "dónde",
        "direccion",
        "dirección"
    ]:

        return (
            "📍 *UBICACIÓN DE VENTUS*\n\n"

            "VENTUS está ubicado en *Wanchaq - Cusco*.\n\n"

            "Su ubicación permite tener acceso a diferentes "
            "servicios y vías de conexión de la ciudad.\n\n"

            "📲 Si deseas recibir la ubicación exacta y orientación "
            "para llegar, escribe *6* y un asesor podrá ayudarte."
        )


    # OPCIÓN 6
    if texto in [
        "6",
        "asesor",
        "asesora",
        "contacto",
        "vendedor",
        "ventas",
        "quiero comprar",
        "comprar"
    ]:

        return (
            "👨‍💼 *ASESOR VENTUS*\n\n"

            "Excelente. Podemos ayudarte con información "
            "sobre disponibilidad, distribución, precios y "
            "proceso de compra.\n\n"

            "📲 Un asesor de BONET CONTRATISTAS GENERALES "
            "se pondrá en contacto contigo.\n\n"

            "Gracias por tu interés en *VENTUS* 🏢"
        )


    # PALABRAS CLAVE AIRBNB
    if "airbnb" in texto or "alquiler" in texto:

        return responder("4")


    # PALABRAS CLAVE 501 / 502
    if "501" in texto or "502" in texto:

        return responder("3")


    # SI NO ENTIENDE
    return (
        "Disculpa, no pude identificar tu opción. 😊\n\n"
        "Por favor responde con uno de estos números:\n\n"
        "1️⃣ Conocer VENTUS\n"
        "2️⃣ Departamentos disponibles\n"
        "3️⃣ Departamentos 501 y 502\n"
        "4️⃣ Airbnb / alquiler temporal\n"
        "5️⃣ Ubicación\n"
        "6️⃣ Hablar con un asesor"
    )


# ==============================
# PÁGINA PRINCIPAL
# ==============================

@app.route("/", methods=["GET"])
def home():

    return "Chat Bot Ventus-Bonet activo"


# ==============================
# VERIFICACIÓN DEL WEBHOOK
# ==============================

@app.route("/webhook", methods=["GET"])
def verify():

    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:

        return challenge, 200

    return "Forbidden", 403


# ==============================
# RECIBIR MENSAJES
# ==============================

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

                incoming_text = message["text"]["body"]

                print("MENSAJE:", incoming_text)

                print("REMITENTE:", sender)

                reply = responder(incoming_text)

                send_whatsapp_message(
                    sender,
                    reply
                )

    except Exception as e:

        print("ERROR:", e)

    return "EVENT_RECEIVED", 200


# ==============================
# EJECUTAR
# ==============================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
