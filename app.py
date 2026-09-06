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
        "🏢 *DEPARTAMENTOS VENTUS*\n\n"

        "Actualmente contamos con dos departamentos destacados:\n\n"

        "🔹 *DEPARTAMENTO 501 – TIPO 3*\n"
        "📐 Área: *127.10 m²*\n"
        "🏙️ Ubicación: *Fachada*\n"
        "🏠 Incluye *aires/azotea de uso exclusivo*\n"
        "➕ En el área de aires se contempla *un ambiente adicional*.\n\n"

        "🔹 *DEPARTAMENTO 502 – TIPO 4*\n"
        "📐 Área: *124.42 m²*\n"
        "🏙️ Ubicación: *Interior*\n"
        "🏠 Incluye *aires/azotea de uso exclusivo*\n"
        "➕ En el área de aires se contempla *un ambiente adicional*.\n\n"

        "💬 Para conocer *precio, forma de pago y disponibilidad actual*, "
        "escribe *6* para hablar con un asesor."
    )
