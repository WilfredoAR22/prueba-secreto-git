import os

print("PRUEBA DE SEGURIDAD - SECRETO SEGURO")
print("------------------------------------")

API_KEY = os.environ.get("API_KEY")

if API_KEY:
    print("Clave de API obtenida correctamente")
    print("Estado: Secreto cargado desde variable de entorno")
else:
    print("Error: No se encontro la variable API_KEY")
