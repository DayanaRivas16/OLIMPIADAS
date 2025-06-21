#CODIGO
print("INICIO DEL PROGRAMA")
numero= int(input("Ingresa un número entero: "))

if numero % 2 == 0 and numero % 3 == 0:
    print("Es par y múltiplo de 3")
elif numero % 2 == 0:
    print("Es par pero no es múltiplo de 3")
elif numero % 3 == 0:
    print("Es impar y múltiplo de 3")
else:
    print("Es impar y no es múltiplo de 3")

print("FIN DEL PROGRAMA")

    