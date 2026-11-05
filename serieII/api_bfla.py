
from flask import Flask, jsonify, request

app = Flask(__name__)

# Usuarios ficticios del laboratorio
usuarios = {
    "usuario1": {"rol": "usuario"},
    "admin": {"rol": "administrador"}
}

@app.route("/api/admin/configuracion", methods=["GET"])
def configuracion():

    usuario = request.headers.get("X-Usuario")

    if usuario not in usuarios:
        return jsonify({
            "error": "Usuario no autenticado"
        }), 401

    # Vulnerabilidad BFLA:
    # No se verifica que el usuario sea administrador

    return jsonify({
        "mensaje": "Acceso a configuracion administrativa",
        "configuracion": "Panel de administracion"
    }), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5003, debug=False)
