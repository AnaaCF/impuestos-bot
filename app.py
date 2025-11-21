from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Estado del reporte: guardamos la última vez que tu PC confirmó "OK"
last_ok_timestamp = 0

@app.route("/")
def home():
    return "Bot running"

@app.route("/ok", methods=["POST"])
def ok():
    global last_ok_timestamp
    last_ok_timestamp = time.time()
    return jsonify({"status": "received"})
