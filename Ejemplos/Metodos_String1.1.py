
# Trabajar con Strings
"""Los strings son secuencias de caracteres de texto.
Todos los objetos en python se engloban en dos categorias: mutables o inmutables.
Los tipos basicos mutables son las listas, los diccionarios y los sets.
Los tipos basicos inmutables son los numeros, los strings y las tuplas. 
Los objetos mutables pueden ser cambiados en el mismo objeto, mientras que los inmutables no. 
"""
# Para concatenar textos se hace con "+" o simplemente con una coma.
# Si ponemos coma nos pone entre los textos un espacio con + no lo hace 

print("Esta frase" , "termina aqui.")
print("Esta frase" + "termina aqui.")

# Concatenacion de y multiplicacion de strings
a = "uno"
b = "dos"
c = a + b  # c es "unodos"
c = a * 3  # c es "unounouno"

# -----------------------------------------------------

# Metodos de los strings: 

# lower(): Convierte en minuscula un string
s_texto1 = "ESTE TEXTO ESTA INICIALMENTE EN MAYUSCULAS"
print(s_texto1.lower())

