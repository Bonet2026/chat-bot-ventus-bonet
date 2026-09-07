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
# OPCIÓN 3
    if texto in ["3", "501", "502", "departamento 501", "departamento 502"]:
        return (
            "🏢 *INFORMACIÓN DE LOS DEPARTAMENTOS 501 Y 502*\n\n"

            "🔹 *DEPARTAMENTO 501 – TIPO 3*\n"
            "📐 Área: *127.10 m²*\n"
            "🏙️ Ubicación: *Fachada*\n"
            "🏠 Aires/azotea de uso exclusivo\n"
            "➕ Ambiente adicional contemplado en el área de aires.\n\n"

            "🔹 *DEPARTAMENTO 502 – TIPO 4*\n"
            "📐 Área: *124.42 m²*\n"
            "🏙️ Ubicación: *Interior*\n"
            "🏠 Aires/azotea de uso exclusivo\n"
            "➕ Ambiente adicional contemplado en el área de aires.\n\n"

            "💬 Para conocer precios, forma de pago y disponibilidad actual, "
            "escribe *6* para hablar con un asesor."
        )
# OPCIÓN 4
if texto in ["4", "airbnb", "alquiler", "alquiler temporal"]:

    return (
        "🏠 *VENTUS PARA AIRBNB / ALQUILER TEMPORAL*\n\n"

        "VENTUS está pensado no solo para vivienda, sino también "
        "como una alternativa para quienes buscan utilizar su departamento "
        "para alquiler temporal tipo Airbnb.\n\n"

        "⭐ *¿Por qué VENTUS puede ser una buena alternativa?*\n\n"

        "• Departamentos modernos y funcionales.\n"
        "• Ubicación en Wanchaq – Cusco.\n"
        "• Los departamentos 501 y 502 cuentan con "
        "aires/azotea de uso exclusivo.\n"
        "• En el área de aires se contempla un ambiente adicional.\n\n"

        "📌 El uso para alquiler temporal dependerá de las condiciones "
        "y decisiones del propietario y de la normativa aplicable.\n\n"

        "💬 Si deseas conocer precios, forma de pago y disponibilidad, "
        "escribe *6* para hablar con un asesor."
    )
    # OPCIÓN 5
if texto in ["5", "ubicacion", "ubicación", "donde", "dónde", "dirección"]:

    return (
        "📍 *UBICACIÓN DEL PROYECTO VENTUS*\n\n"

        "🏢 *VENTUS* se encuentra en *Wanchaq – Cusco*.\n\n"

        "📌 Su ubicación permite contar con acceso a "
        "diferentes servicios y puntos importantes de la ciudad.\n\n"

        "🏪 Cerca del proyecto encontrarás referencias como "
        "supermercados, bancos, clínicas y vías de acceso hacia "
        "el centro de Cusco.\n\n"

        "⚽ Una referencia cercana es el campo deportivo "
        "*El Hueco*.\n\n"

        "🚗 La ubicación es una de las características importantes "
        "de VENTUS para vivir o considerar el alquiler temporal.\n\n"

        "💬 Si deseas conocer la ubicación exacta y recibir "
        "orientación, escribe *6* para hablar con un asesor."
    )
# OPCIÓN 6
if texto in ["6", "asesor", "asesora", "asesor comercial", "contactar"]:

    return (
        "👨‍💼 *ASESOR COMERCIAL VENTUS*\n\n"

        "Gracias por tu interés en *VENTUS*.\n\n"

        "Un asesor de BONET puede ayudarte con información sobre:\n\n"

        "🏢 Departamentos disponibles\n"
        "💰 Precios y formas de pago\n"
        "📐 Planos y distribución\n"
        "📍 Ubicación del proyecto\n"
        "🏠 Información sobre alquiler temporal / Airbnb\n"
        "📅 Coordinación de visita al proyecto\n\n"

        "📲 *Contáctanos directamente:*\n"
        "WhatsApp: *914 230 705*\n\n"

        "👉 Déjanos tu consulta y un asesor continuará contigo."
    )
