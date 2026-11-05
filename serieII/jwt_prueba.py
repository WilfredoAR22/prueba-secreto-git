
import base64
import json

# JWT ficticio de laboratorio
header = {
    "alg": "HS256",
    "typ": "JWT"
}

payload = {
    "sub": "usuario1",
    "rol": "usuario",
    "iss": "api-laboratorio",
    "aud": "api-laboratorio",
    "exp": 1893456000
}

def codificar(datos):
    contenido = json.dumps(datos).encode("utf-8")
    return base64.urlsafe_b64encode(contenido).decode().rstrip("=")

# Token de ejemplo sin firma valida
token = codificar(header) + "." + codificar(payload) + ".firma_ficticia"

print("PRUEBA DE SEGURIDAD - JWT")
print("------------------------")

print("\nToken de laboratorio:")
print(token)

partes = token.split(".")

def decodificar(parte):
    parte += "=" * (-len(parte) % 4)
    return json.loads(base64.urlsafe_b64decode(parte))

print("\nENCABEZADO DECODIFICADO:")
print(json.dumps(decodificar(partes[0]), indent=4))

print("\nCARGA UTIL DECODIFICADA:")
print(json.dumps(decodificar(partes[1]), indent=4))

print("\nALGORITMO IDENTIFICADO:")
print(decodificar(partes[0])["alg"])
