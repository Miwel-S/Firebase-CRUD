import pyrebase
import requests

#Esta informacion es publica y todas las apps con Firebase la tienen
firebase_config = {
    "apiKey": "TU_API_KEY",
    "authDomain": "tu-proyecto.firebaseapp.com",
    "databaseURL": "https://tu-proyecto.firebaseio.com",
    "storageBucket": "tu-proyecto.appspot.com",
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Login del usuario
email = "usuario@ejemplo.com"
password = "contraseña123"
user = auth.sign_in_with_email_and_password(email, password)

# Obtenemos el token de autenticación
id_token = user['idToken']

# Ahora hacemos un request al backend FastAPI
response = requests.get(
    "http://TU_IP_PUBLICA:8000/data/usuarios",
    headers={"Authorization": f"Bearer {id_token}"}
)

print(response.json())