usuario=["Camilo", "Sara","Luisa"]
dispositivos=["Laptop", "Tablet", "Smartphone"]

if "Luisa" in usuario:
    usuario.append("David")
    
elif "smartphone" in dispositivos:
    dispositivos.append("Smartwatch")

elif "Sara" in usuario:
    usuario.remove ("Sara")
    
elif len (dispositivos)>3:
    dispositivos.pop(0)
    
elif "Camilo" in usuario:
    usuario.remove("Camilo")
    usuario.append("Andres")
else:
    print("Todo esta bien")

    
soporte_tecnico=usuario[:2]
dispositivos_moviles=dispositivos[:-2]

if "Smartwatch" in dispositivos_moviles:
    nuevo_dispositivo=("Smartwatch","Disponible")
    
    if soporte_tecnico[0] == "Andrés":
    soporte_tecnico.append("Nivel Avanzado")
elif len(soporte_tecnico) > 1 and soporte_tecnico[1] == "Andrés":
    soporte_tecnico.append("Nivel Avanzado")


if dispositivos[0] == "Tablet" or dispositivos[1] == "Tablet" or dispositivos[2] == "Tablet" or (len(dispositivos) > 3 and dispositivos[3] == "Tablet"):
    registro_usuario = {
        "estado": "Activo",
        "equipo": "Tablet",
        "tecnico": "Andrés"
    }


registro_usuario_creado = False
if dispositivos[0] == "Tablet" or dispositivos[1] == "Tablet" or dispositivos[2] == "Tablet" or (len(dispositivos) > 3 and dispositivos[3] == "Tablet"):
    registro_usuario_creado = True

if registro_usuario_creado == True:
    registro_usuario["último_ingreso"] = "18/06/2025"

impresora_esta = False
if dispositivos[0] == "Impresora":
    impresora_esta = True
elif dispositivos[1] == "Impresora":
    impresora_esta = True
elif dispositivos[2] == "Impresora":
    impresora_esta = True
elif len(dispositivos) > 3 and dispositivos[3] == "Impresora":
    impresora_esta = True
    
    




    




    
