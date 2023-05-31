# Pedir la longitud en metros
longitud_metros = float(input("Ingrese la longitud en metros: "))

# Convertir metros a pies
pies = int(longitud_metros * 3.28084)

# Convertir metros restantes a pulgadas
pulgadas = int((longitud_metros * 3.28084 - pies) * 12)

# Imprimir el resultado
print("La longitud de", longitud_metros, "metros equivale a", pies, "pies y", pulgadas, "pulgadas.")