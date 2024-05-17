# Variables en Python

# Lo ideal es declarar antes las variables antes de usarlas para que no de error el codigo
# y para que sea mas facil de leer y entender el codigo
# Se puede declarar una variable sin asignarle un valor, pero no se puede usar esa variable
# hasta que se le asigne un valor
# ------------------------------------------------------------------------------------------

# Ejemplo 1: Declaracion de varible numerica entera:
n_edad = 22

# Ejemplo 2: Declaracion de variable numerica flotante(decimal):
n_precio = 22.5

# Ejemplo 3: Declaracion de variable tipo string: 
s_nombre = 'Juan es "amigo" mio'

# Ejemplo 4: Declaracion de variable tipo string en varias lineas: 
s_textoLargo = """Esto es un mensaje
...con tres saltos
... de linea"""

#Ejemplo 5: Sobreescribimos el valor de la varible s_edad y ahora la ponemos en como string:
s_edad = '22'

# Ejemplo 6: Declaracion de constante 
NUMEROPI = 3.141559

# Ejemplo 7: Declaracion de booleanos
b_esVerdadero = True
is_casado = False

#True == 1 y False == 0
True == 1
False == 0

print(True + 2)

# Ejemplo 8: Declaracion de cuando se valida una condicion, Python devuelve True o False: 
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Ejemplo 9: Declaracion multiple
# En una sola linea instruccion, estamos declarando tres variables: a, b, c, y asignandoles un valor concreto a cada una
a, b, c = 'String', 20, True

# Seria como poner: 
a = 'String'
b = 20
c = True

# Para verificar el tipo de cualquier objeto en python, usamos la funcion type() :

print(type(n_edad))
print(type(n_precio))
print(type(s_nombre))
print(type(NUMEROPI))
print(type(b_esVerdadero))
print(type(is_casado))

