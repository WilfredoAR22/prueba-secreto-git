
from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos ficticios para el laboratorio
cuentas = {
    1001: {"propietario": "usuario1", "saldo": 5000},
    1002: {"propietario": "usuario2", "saldo": 12000}
}

@app.route("/api/cuentas/<int:id_cuenta>", methods=["GET"])
def consultar_cuenta(id_cuenta):

    # Simulamos la identidad del usuario autenticado
    usuario = request.headers.get("X-Usuario")

    if not usuario:
        return jsonify({"error": "Usuario no autenticado"}), 401

    cuenta = cuentas.get(id_cuenta)

    if not cuenta:
        return jsonify({"error": "Cuenta no encontrada"}), 404

    # Vulnerabilidad BOLA:
    # No se verifica que la cuenta pertenezca al usuario
    return jsonify(cuenta), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
