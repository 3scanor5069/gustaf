edad = int(input("ingrese su edad"))
if edad >= 0 and  edad <= 5:
    print ("Bebé")
elif  edad >= 6 and  edad <= 12:
    print ("Niño")
elif edad >= 13 and  edad <= 18:
    print ("Adolescente")
elif edad >= 19 and  edad <= 45:
    print ("Adulto")
elif edad >= 46 and  edad <= 90:
    print ("mayor")
elif edad > 96:
    print ("mayor de edad")
elif edad <0:
    print ("ingrese una edad entre el rango establecido")
elif edad >96:
    print ("Felicidades eres de los concursantes finalistas junto con Amparo Grisales y Diego Jaramillo ")

