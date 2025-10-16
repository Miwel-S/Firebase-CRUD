import os
import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials,db

class FirebaseService:
    def __init__(self):   
        load_dotenv()
        self.creds_json=os.getenv("FIREBASE_CREDS_JSON")
        self.db_url=os.getenv("FIREBASE_DB_URL")

        if not self.creds_json:
            raise FileExistsError("No se encontro el archivo de credenciales.")
        if not self.db_url:
            raise FileExistsError("No existe la variable de la url de la base de datos")
        
        if not firebase_admin._apps:
            cred= credentials.Certificate(str(self.creds_json))
            firebase_admin.initialize_app(cred,{"databaseURL":self.db_url})
        
        #Referencia raiz, para acceder a cualquier nodo del arbol
        self.root_ref=db.reference("/")

    def create(self, path: str, data: dict):
        if not path:
            raise ValueError("Debes especificar la ruta")
        self.root_ref.child(path).set(data)

    def read(self,path:str):
        if not path:
            raise ValueError("Debes especificar la ruta")
        ref=self.root_ref.child(path)
        data=ref.get()
        if data is None:
            return None
        if not isinstance(data,dict):
            raise ValueError("Formato incorrecto, se esperaba un dict")
        return data
    
    def update(self, path:str, new_data:dict):
        if not path:
            raise ValueError("Debes especificar la ruta")
        if not isinstance(new_data, dict):
            raise ValueError("Se esperaba un dict")
        self.root_ref.child(path).update(new_data)
        

    def delete(self, path:str):
        if not path:
            raise ValueError("Debes especificar la ruta")
        self.root_ref.child(path).delete()