# Se usa para generar una lista nueva en base a una existente o a un patron de creacion
# Se hace en una sola linea, en vez de usar un bucle con .append()

# 1 fase = cracion de listas 
# 2 fase = transformacion o llenado de listas mediante un iterador con append()

numeros = [1,2,3,4] # = source
cuadrados = []


for n in numeros:
    cuadrados.append(n**2)

print(cuadrados)

# lo mismo pero con compresion 
# SINTAXIS = [expresion for elemento in iterable expresion de filtrado ]
# expresion = el metodo de transformacion o copiado 

cuadrados_compresion = [(n**2) for n in numeros]
print(cuadrados_compresion)

# Ejemplo de expresiones 

#Ejemplo 1 
palabras =["python", "pseint", "sql"]
longitudes = [(len(palabra)) for palabra in palabras]
# print(longitudes)

#Ejemplo 2
texto_numeros = ["3","12","109"]
numeros = [(int(n)) for n in texto_numeros]

#Ejemplo 3
decimales = [19.9999, 31.555, 89.1]

#Ejemplo 4
decimales_redondeados = [ (round(decimal,1)) for decimal in decimales]
print(decimales_redondeados)

#Ejemplo 5
nuevos_decimales_redondeados = []
for decimal in decimales :
    decimal_redondeado  = round(decimal,1)
    nuevos_decimales_redondeados.append(decimal_redondeado)
print(nuevos_decimales_redondeados)


