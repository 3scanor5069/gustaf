sueldo = float(input("ingrese su salario"))
años = int(input("ingrese el tiempo que lleva en la empresa"))
if años < 1:
    utilidad = sueldo * 0.05  
    print("su sueldo es:" , utilidad)
elif años > 1 or años < 2:
    utilidad = sueldo * 0.07 
    print("su sueldo es:" , utilidad)
elif años > 2 or edad < 5:
    utilidad = sueldo * 0.10 
    print("su sueldo es:" , utilidad)
elif años > 5 or años < 10:
    utilidad = sueldo * 0.15  
    print("su sueldo es:" , utilidad)
elif años > 10:
    utilidad = sueldo * 0.20  
    print("su sueldo es:" , utilidad)