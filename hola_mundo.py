# 1. Imprime "Hola, mundo"

print("Hola, mundo")

# 2. Imprime "Hola, Valeria" con el nombre en una variable

nombre = "Valeria"

print("Hola,", nombre) # con una coma

print("Hola, "+nombre) # con un +

# 3. Imprimir "Hola 156!" con el número en una variable

numero = 1105

print("Hola ",numero, "!") # con una coma

#print("Hola "+ numero + "!") # con un + -- este debería arrojar un error!, corrígelo con conversión
print("Hola " +str(numero)+ "!")
# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables

comida1 = "empanadas"

comida2 = "chipa so'o"

print("Me encanta comer {} y {}".format(comida1, comida2)) # con .format()

print(f"Me encanta comer {comida1} y {comida2}") # con una cadena f

#bonus, insertar un espacio (" " despues de cada caracter)
print(" ".join(comida1))
