from argon2 import PasswordHasher

ph = PasswordHasher()
contrasena = "SeguridadUMG2026!"

hash1 = ph.hash(contrasena)
hash2 = ph.hash(contrasena)

print("PRUEBA DE SEGURIDAD - ARGON2ID")
print("-----------------------------")

print("\nPrimer hash:")
print(hash1)

print("\nSegundo hash:")
print(hash2)

print("\n¿Los hashes son iguales?")
print(hash1 == hash2)

print("\nVerificacion de contrasena:")
print(ph.verify(hash1, contrasena))
