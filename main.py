from firebase_service import FirebaseService

def main():
    
    storage=FirebaseService()

    #Crear datos
    storage.create("Usuarios/miguel",{"Nombre":"Miguel",
                                      "Edad":"20",
                                      "Carrera":"Ingenieria Electrica"
                                      })
    
    storage.create("Usuarios/juanito",{"Nombre":"Juanito",
                                      "Edad":"12",
                                      "Carrera":"Ingenieria Mecanica"
                                      })

    #Leer datos e imprimirlos en consola
    datos=storage.read("Usuarios/miguel")
    print(datos)
    
    #Actualizar algunos datos
    storage.update("Usuarios/miguel",{"Edad":"17",
                                      "Carrera":"Ingenieria Electronica"
                                      })

    #Eliminar datos
    storage.delete('Usuarios/miguel')
    storage.delete("Usuarios/juanito")

if __name__=="__main__":
    main()