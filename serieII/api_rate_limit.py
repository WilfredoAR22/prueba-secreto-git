
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/login", methods=["POST"])
def login():

    datos = request.get_json(silent=True) or {}

    usuario = datos.get("user")
    clave = datos.get("pass")

    if usuario == "admin" and clave == "UMG2026":
        return jsonify({"mensaje": "Acceso autorizado"}), 200

    return jsonify({"error": "Credenciales incorrectas"}), 401

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=False)
