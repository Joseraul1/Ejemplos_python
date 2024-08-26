a = True
b = False
resultado = a and b
# Print(resultado)

resultado = a or b
# Print(resultado)

resultado = not a 
print(resultado)

# -----------------------------------
# Sintaxis simplificada para varios operadores logicos
edad = int(input("Introduce tu edad: "))

# Veintes = edad >= 20 and edad < 30
# print(veintes)
# Treintas = edad >= 30 and edad < 40
# print (treintas)

if(20 <= edad < 30) or (30 <= edad < 40):
    print("Dentro del rango de (20\'s) o (30\'s)")  
#   if veintes:
#       print("Dentro del rango de (20\'s)")
#   elif treintas:
#       print("Dentro del rango de (30\'s)")
#   else:
#       print("No estás en ninguno de los rangos")

else:
    print("No esta dentro de los 20's ni 30's")