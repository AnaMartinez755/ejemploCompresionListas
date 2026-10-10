# SINTAXIS = [expresion for elemento in iterable expresion de filtrado if : else]

#Filtrar los strings que empiezan con una letra especifica
nombres = ['Ana','Juan','Emanuel']
nombres_con_a = [nombre for nombre in nombres if nombre.startswith('A')]
print(nombres_con_a)

numeros = [1,2,3,4] # = source
cuadrados_compresion_mayores3 = [(n**2) for n in numeros if n>=3]
print(cuadrados_compresion_mayores3)


#Filtrado de numeros pares
numeros = [1,2,3,4,5,6,7,8,9,10]
pares = [n for n in numeros if n % 2 ==0 ]
print(pares)

#Etiquetado de numeros (par/impar)
etiquetas = [("par" if n%2 ==0 else "impar") for n in numeros]
print(etiquetas)

#Aplicar un metodo 
mayusculas = [(nombre.upper()) for nombre in nombres]
print(mayusculas)


colores = ['rojo','azul','amarillo']
tallas = ['S','M']

combinaciones = [(f'{color}-{talla}') for color in colores for talla in tallas]
print(combinaciones)