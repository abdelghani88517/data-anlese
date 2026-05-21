from cryptography.fernet import Fernet
# Génération de la clé
key = Fernet.generate_key()

# Affichage de la clé
print(key)