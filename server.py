from fastapi import FastAPI, HTTPException, Header
from firebase_admin import credentials, initialize_app, auth
from firebase_service import FirebaseService  # Tu clase CRUD
import firebase_admin

# Inicializar Firebase Admin una sola vez
if not firebase_admin._apps:
    cred = credentials.Certificate("service_account.json")
    initialize_app(cred, {"databaseURL": "https://tu-db.firebaseio.com"})

firebase_service = FirebaseService()
app = FastAPI(title="Backend seguro con Firebase Auth")

# ✅ Middleware o función para validar tokens
def verificar_token(authorization: str):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token no proporcionado o inválido")
    token = authorization.split(" ")[1]
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

# 📥 Ruta de lectura protegida
@app.get("/datos/{path}")
def leer_datos(path: str, authorization: str = Header(None)):
    user = verificar_token(authorization)
    data = firebase_service.read(path)
    return {"uid": user["uid"], "data": data}

# 📤 Ruta de escritura protegida
@app.post("/datos/{path}")
def escribir_datos(path: str, data: dict, authorization: str = Header(None)):
    user = verificar_token(authorization)
    firebase_service.create(path, data)
    return {"status": "ok", "uid": user["uid"]}