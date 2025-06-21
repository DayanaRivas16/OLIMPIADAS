edad = int(input("Ingresa tu edad: "))


if edad >= 0 and edad <= 12:
    print("Eres un Niño")
elif edad >= 13 and edad <= 17:
    print("Eres un Adolescente")
elif edad >= 18 and edad <= 64:
    print("Eres un Adulto")
elif edad >= 65:
    print("Eres un Adulto Mayor")
else:
    print("Edad no válida")
    
