# find() retorna la posicion de la primera similitud de la substring

cadenaDeTexto = "Es peor cometer una injusticia que padecerla porque quien la comete se convierte en injusto y quien la padece no"
print(cadenaDeTexto.find('quien'))

# Devolveria: 52

# -------------------------------------------------------------------------

# rfind() retorna la ultima posicion de la similitud de la substring

cadenaDeTexto = "Es peor cometer una injusticia que padecerla porque quien la comete se convierte en injusto y quien la padece no"
print(cadenaDeTexto.rfind('quien'))

# Devolveria: 94
# Si, el substring no es encontrado retorna -1
# -------------------------------------------------------------------------

# replace. Devuelve una cadena de caracteres donde un valor especificado se reemplaza con un valor especificado

miString = "Esto es bonito. Esto es bueno"
newString = miString.replace("es", "FUE")
print(newString)

# Devolveria: Esto FUE bonito. Esto FUE bueno
# -------------------------------------------------------------------------