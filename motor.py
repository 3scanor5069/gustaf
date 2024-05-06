motor = int(input("ingrese la temperatura de motor"))
if motor == 0:
    print("el motor está apagado")
elif motor < 80:
   print("el motor está encendido")