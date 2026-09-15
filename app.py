from flask import Flask, request
import os
import requests

app = Flask(__name__)


# ============================================================
# CONFIGURACIÓN
# ============================================================

VERIFY_TOKEN = os.environ.get(
    "VERIFY_TOKEN",
    "ventus_bonet_webhook_2026"
)

WHATSAPP_TOKEN = os.environ.get("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.environ.get("PHONE_NUMBER_ID")


# ============================================================
# ENVIAR MENSAJES POR WHATSAPP
# ============================================================

def send_whatsapp_message(to, text):

    if not WHATSAPP_TOKEN:
        print("ERROR: WHATSAPP_TOKEN no configurado")
        return False

    if not PHONE_NUMBER_ID:
        print("ERROR: PHONE_NUMBER_ID no configurado")
        return False

    url = (
        f"https://graph.facebook.com/v26.0/"
        f"{PHONE_NUMBER_ID}/messages"
    )

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to,
        "type": "text",
        "text": {
            "preview_url": False,
            "body": text
        }
    }

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=20
        )

        print(
            "Respuesta WhatsApp:",
            response.status_code,
            response.text
        )

        return response.ok

    except Exception as error:

        print("Error enviando mensaje:", error)

        return False


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def menu_principal():

    return (
        "🏢 *VENTUS - BONET CONTRATISTAS GENERALES*\n\n"

        "👋 Bienvenido al asistente de información del "
        "*Proyecto Ventus*.\n\n"

        "Estamos para ayudarte a conocer nuestros departamentos "
        "en preventa y las posibilidades de inversión.\n\n"

        "📋 *¿Qué deseas conocer?*\n\n"

        "1️⃣ Información general de VENTUS\n"
        "2️⃣ Departamentos disponibles\n"
        "3️⃣ Información de los departamentos 501 y 502\n"
        "4️⃣ VENTUS para Airbnb / alquiler temporal\n"
        "5️⃣ Ubicación del proyecto\n"
        "6️⃣ Hablar con un asesor\n\n"

        "👉 Responde con el número de la opción que deseas."
    )


# ============================================================
# RESPUESTAS DEL CHATBOT
# ============================================================

def responder(texto):

    if not texto:
        return menu_principal()

    texto = texto.lower().strip()


    # --------------------------------------------------------
    # SALUDO
    # --------------------------------------------------------

    if texto in [
        "hola",
        "ola",
        "buenas",
        "buenos dias",
        "buenos días",
        "buenas tardes",
        "buenas noches",
        "inicio",
        "menu",
        "menú"
    ]:

        return menu_principal()


    # --------------------------------------------------------
    # OPCIÓN 1
    # --------------------------------------------------------

    if texto in [
        "1",
        "ventus",
        "proyecto",
        "informacion",
        "información"
    ]:

        return (
            "🏢 *VENTUS - BONET CONTRATISTAS GENERALES*\n\n"

            "✨ *Tu nuevo espacio en Wanchaq - Cusco.*\n\n"

            "VENTUS es un proyecto multifamiliar pensado para "
            "quienes buscan una vivienda moderna, funcional y "
            "bien ubicada.\n\n"

            "🏠 Además, sus departamentos pueden ser considerados "
            "como una alternativa para alquiler temporal tipo Airbnb, "
            "según las condiciones del propietario y la normativa "
            "aplicable.\n\n"

            "⭐ *Características destacadas:*\n"

            "• Departamentos modernos y funcionales.\n"
            "• Ubicación en Wanchaq - Cusco.\n"
            "• Diferentes áreas y distribuciones.\n"
            "• Proyecto en etapa de preventa.\n"
            "• Pensado para vivienda e inversión.\n\n"

            "🧭 *¿Qué deseas conocer?*\n\n"

            "👉 Escribe *2* para ver los departamentos disponibles.\n"
            "👉 Escribe *3* para conocer los departamentos 501 y 502.\n"
            "👉 Escribe *4* para conocer el potencial para Airbnb.\n"
            "👉 Escribe *5* para conocer la ubicación.\n"
            "👉 Escribe *6* para hablar con un asesor."
        )


    # --------------------------------------------------------
    # OPCIÓN 2
    # --------------------------------------------------------

    if texto in [
        "2",
        "departamentos",
        "departamento",
        "disponibles"
    ]:

        return (
            "🏢 *DEPARTAMENTOS VENTUS*\n\n"

            "Actualmente contamos con diferentes alternativas "
            "de departamentos dentro del proyecto.\n\n"

            "Entre las unidades que podemos mostrarte están:\n\n"

            "🔹 *DEPARTAMENTO 501 - TIPO 3*\n"
            "📐 Área referencial: *127.10 m²*\n"
            "🏙️ Ubicación: *Fachada*\n"
            "🏡 Incluye área de aires/azotea de uso exclusivo.\n\n"

            "🔹 *DEPARTAMENTO 502 - TIPO 4*\n"
            "📐 Área referencial: *124.42 m²*\n"
            "🏙️ Ubicación: *Interior*\n"
            "🏡 Incluye área de aires/azotea de uso exclusivo.\n\n"

            "💬 Para conocer precio, forma de pago y disponibilidad "
            "actual, escribe *6* para hablar con un asesor."
        )


    # --------------------------------------------------------
    # OPCIÓN 3
    # --------------------------------------------------------

    if texto in [
        "3",
        "501",
        "502",
        "departamento 501",
        "departamento 502"
    ]:

        return (
            "🏢 *INFORMACIÓN DE LOS DEPARTAMENTOS 501 Y 502*\n\n"

            "🔷 *DEPARTAMENTO 501 - TIPO 3*\n\n"

            "📐 Área referencial: *127.10 m²*\n"
            "🏙️ Ubicación: *Fachada*\n"
            "🏡 Área de aires/azotea de uso exclusivo.\n\n"

            "🔷 *DEPARTAMENTO 502 - TIPO 4*\n\n"

            "📐 Área referencial: *124.42 m²*\n"
            "🏙️ Ubicación: *Interior*\n"
            "🏡 Área de aires/azotea de uso exclusivo.\n\n"

            "📲 Si deseas conocer precio, planos o disponibilidad, "
            "escribe *6* para comunicarte con un asesor."
        )


    # --------------------------------------------------------
    # OPCIÓN 4
    # --------------------------------------------------------

    if texto in [
        "4",
        "airbnb",
        "alquiler",
        "alquiler temporal",
        "inversion",
        "inversión"
    ]:

        return (
            "💼 *VENTUS COMO ALTERNATIVA DE INVERSIÓN*\n\n"

            "El proyecto VENTUS también está orientado a compradores "
            "que desean evaluar sus departamentos para alquiler "
            "temporal tipo Airbnb.\n\n"

            "📍 Su ubicación en Wanchaq - Cusco permite considerar "
            "una estrategia dirigida tanto a vivienda como a "
            "alquiler temporal.\n\n"

            "Cada propietario administrará de manera independiente "
            "su departamento y su operación de alquiler.\n\n"

            "📊 Los resultados y rentabilidad dependen del precio "
            "de compra, ocupación, tarifa por noche, gastos y forma "
            "de administración.\n\n"

            "👉 Escribe *6* si deseas conversar con un asesor sobre "
            "una posible inversión."
        )


    # --------------------------------------------------------
    # OPCIÓN 5
    # --------------------------------------------------------

    if texto in [
        "5",
        "ubicacion",
        "ubicación",
        "direccion",
        "dirección",
        "wanchaq"
    ]:

        return (
            "📍 *UBICACIÓN DEL PROYECTO VENTUS*\n\n"

            "El proyecto se encuentra en el distrito de "
            "*Wanchaq - Cusco*.\n\n"

            "📌 Sector: Av. Jorge Chávez.\n\n"

            "La ubicación permite acceso a diferentes servicios "
            "y zonas importantes de la ciudad.\n\n"

            "👉 Escribe *6* si deseas coordinar información adicional "
            "o una atención con nuestro equipo."
        )


    # --------------------------------------------------------
    # OPCIÓN 6
    # --------------------------------------------------------

    if texto in [
        "6",
        "asesor",
        "asesora",
        "vendedor",
        "ventas",
        "comprar",
        "precio",
        "precios",
        "cotizacion",
        "cotización"
    ]:

        return (
            "👨‍💼 *ASESOR COMERCIAL VENTUS*\n\n"

            "Gracias por tu interés en nuestro proyecto.\n\n"

            "Un asesor de *Bonet Contratistas Generales S.A.C.* "
            "podrá brindarte información sobre:\n\n"

            "✅ Disponibilidad actual.\n"
            "✅ Precios de preventa.\n"
            "✅ Formas de pago.\n"
            "✅ Planos y áreas.\n"
            "✅ Alternativas de inversión.\n"
            "✅ Visita y presentación del proyecto.\n\n"

            "📲 Nuestro equipo continuará tu atención comercial "
            "por este mismo canal."
        )


    # --------------------------------------------------------
    # RESPUESTA NO RECONOCIDA
    # --------------------------------------------------------

    return (
        "🤖 No pude identificar esa opción.\n\n"
        + menu_principal()
    )


# ============================================================
# WEBHOOK - VERIFICACIÓN DE META
# ============================================================

@app.route("/webhook", methods=["GET"])
def verify_webhook():

    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:

        print("Webhook verificado correctamente.")

        return challenge, 200

    print("Error verificando webhook.")

    return "Verification failed", 403


# ============================================================
# WEBHOOK - RECIBIR MENSAJES
# ============================================================

@app.route("/webhook", methods=["POST"])
def receive_webhook():

    try:

        data = request.get_json(silent=True)

        print("Webhook recibido:")
        print(data)

        if not data:
            return "EVENT_RECEIVED", 200

        entry = data.get("entry", [])

        for item in entry:

            changes = item.get("changes", [])

            for change in changes:

                value = change.get("value", {})

                messages = value.get("messages", [])

                for message in messages:

                    sender = message.get("from")

                    message_type = message.get("type")

                    if message_type != "text":
                        continue

                    text_data = message.get("text", {})

                    text = text_data.get("body", "")

                    print(
                        f"Mensaje recibido de {sender}: {text}"
                    )

                    respuesta = responder(text)

                    if sender:
                        send_whatsapp_message(
                            sender,
                            respuesta
                        )

        return "EVENT_RECEIVED", 200

    except Exception as error:

        print("Error procesando webhook:", error)

        # Respondemos 200 para evitar reintentos continuos de Meta
        return "EVENT_RECEIVED", 200


# ============================================================
# PÁGINA PRINCIPAL / HEALTH CHECK
# ============================================================

@app.route("/", methods=["GET"])
def home():

    return (
        "VENTUS BOT - Bonet Contratistas Generales - ONLINE",
        200
    )


@app.route("/health", methods=["GET"])
def health():

    status = {
        "status": "ok",
        "verify_token": bool(VERIFY_TOKEN),
        "whatsapp_token": bool(WHATSAPP_TOKEN),
        "phone_number_id": bool(PHONE_NUMBER_ID)
    }

    return status, 200


# ============================================================
# EJECUCIÓN LOCAL
# ============================================================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
