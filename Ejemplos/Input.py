s_nombreIntroducido = input("Introduzca un nombre: ")

print("Bienvenido", s_nombreIntroducido)

# -------------------------------------

"""IMPORTANTE: Todo lo introducido por input() se considera string, aunque sea un numero, 
por lo que, si necesitamos operar matematicamente con numeros, tendremos que hacer casting: 
"""

s_edad = int(input("introduzca su edad"))

print("El año que viene tendra usted ", s_edad + 1, "años")

