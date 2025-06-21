usuarios=["Camilo", "Sara","Luisa"]
dispositivos=["Laptop", "Tablet", "Smartphone"]

if usuarios[0] == "Luisa" or usuarios[1] == "Luisa" or usuarios[2] == "Luisa":
    usuarios.append("David")

if dispositivos[0] == "Smartphone" or dispositivos[1] == "Smartphone" or dispositivos[2] == "Smartphone":
    dispositivos.append("Smartwatch")


if usuarios[0] == "Sara":
    usuarios.pop(0)
elif usuarios[1] == "Sara":
    usuarios.pop(1)
elif len(usuarios) > 2 and usuarios[2] == "Sara":
    usuarios.pop(2)


if len(dispositivos) > 3:
    dispositivos.pop(0)

if usuarios[0] == "Camilo":
    usuarios.remove("Camilo")
    usuarios.append("Andrés")
elif len(usuarios) > 1 and usuarios[1] == "Camilo":
    usuarios.remove("Camilo")
    usuarios.append("Andrés")
elif len(usuarios) > 2 and usuarios[2] == "Camilo":
    usuarios.remove("Camilo")
    usuarios.append("Andrés")


soporte_tecnico = [usuarios[0], usuarios[1]]


dispositivos_moviles = [dispositivos[-2], dispositivos[-1]]

sw1 = dispositivos_moviles[0] == "Smartwatch"
sw2 = len(dispositivos_moviles) > 1 and dispositivos_moviles[1] == "Smartwatch"

if sw1 or sw2:
    tupla = ("Smartwatch", "Disponible")

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

if impresora_esta == False:
    dispositivos.append("Impresora")


luisa_esta = False
if usuarios[0] == "Luisa":
    luisa_esta = True
elif usuarios[1] == "Luisa":
    luisa_esta = True
elif usuarios[2] == "Luisa":
    luisa_esta = True
elif len(usuarios) > 3 and usuarios[3] == "Luisa":
    luisa_esta = True

if luisa_esta == False:
    usuarios.append("Luisa")

print("usuarios:", usuarios)
print("dispositivos:", dispositivos)
print("soporte_tecnico:", soporte_tecnico)
print("dispositivos_moviles:", dispositivos_moviles)
if sw1 or sw2:
    print("tupla:", tupla)
if registro_usuario_creado == True:
    print("registro_usuario:", registro_usuario)