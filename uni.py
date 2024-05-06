estrato = int(input("ingrese su estrato"))
edad = int(input("ingrese su edad"))
matricula = int(input("ingrese el costo de su matrcula"))

if estrato == 1 and edad < 18:
   resultado = matricula * 0.20 
   print("la matrcula con el descuento aplicado es de", resultado)
elif estrato == 1 and edad > 18:
   resultado = matricula * 0.15 
   print("la matrcula con el descuento aplicado es de", resultado)
elif estrato == 2 and edad < 18:
   resultado = matricula * 0.10 
   print("la matrcula con el descuento aplicado es de", resultado)
elif estrato == 2 and edad > 18:
   resultado = matricula * 0.05 
   print("la matrcula con el descuento aplicado es de", resultado)