## imprime todos los numeros enteros del 1 al 100
for i in range(0, 101, 1):
    print(i)
    
## imprime todos los numeros multiplos de 2 entre 2 y 500
for i in range(2, 501, 2):
    print(i)

## Imprime los numeros enteros del 1 al 100. Si es divisible por 5 imprime "ice ice" en vez del numero. Si es divisible por 10 imprimir "baby"

for i in range(1,101,1):
   
    if (i%10) == 0:
        print("baby")
    elif (i%5) == 0:
        print("ice ice")
    else:
        print(i)

## suma los numeros pares del 0 al 500,000 e imprime la suma total
sum = 0
for i in range(0,500001,2):
    if(i%2==0):
        sum=sum + i
print("La suma total es: ", sum)

## imprime los numeros positivos comenzando desde 2024, en cuenta regresiva de 3 en 3 

for i in range(2024,0, -3):
    print (i)

## establece 3 variables numInicial, numFinal, multiplo. comenzando en numInicial y numFinal imprime los numeros enteros que sean multiplos del multiplo.


numInicial = input("Ingresa el valor del numero inicial: ")
numFinal = input("Ingresa el valor del numero final: ")
multiplo = input("Ingresa el valor del multiplo: ")
numInicial = int(numInicial)
numFinal = int(numFinal) +1 # le sumo 1 porque necesito que me tome el 10
multiplo = int(multiplo)

for i in range(numInicial, numFinal):
    if i%multiplo ==0:
        print(i)
