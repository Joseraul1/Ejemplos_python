# En este apartado vamos a ver los tipos de casting que hay en python

# Forzado de tipos enteros:
x = int(1)      # x Valdra 1
y = int(2.8)    # y Valdra 2 
z = int("3")    # z Valdra 3

# Forzado tipo Float: 
x = float(1)     # x Valdra 1.0
y = float(2.8)   # y Valdra 2.8
z = float("3")   # z Valdra 3.0
w = float("4.2") # z Valdra 4.2

# Forzado de tipo String:
x = str("s1")    # x Valdra 's1'
y = str(2)       # y Valdra '2'
z = str(3.0)     # z Valdra '3.0'

# CASTING. Reconversion de tipos:
# Casting de int a float: 
n_numero = 13
n_numero_2 = float(n_numero)

# Casting de float a int: 
n_numero_3 = 24.87
n_numero_4 = int(n_numero_3)

# Casting de string a int:
s_texto = "15"
n_numero_5 = int(s_texto)

# Casting de int a string: 
n_numero_6 = 22
s_texto_2 = str(n_numero_6)

print(n_numero_2)
print(type(n_numero_2))
print(n_numero_4)
print(type(n_numero_5))
print(s_texto_2)
print(type(s_texto_2))

