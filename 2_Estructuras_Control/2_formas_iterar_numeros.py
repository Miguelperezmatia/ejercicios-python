#   Emplea mecanismos diferentes para imprimir números del 1 al 10 mediante iteración



#   1)  For con rango

for numero in range (1,11):
    print(numero)



#   2)  For de solo lectura

numeros = [1,2,3,4,5,6,7,8,9,10]
for n in numeros:
    print(n)



#   3)  While

n = 1
while(n < 11):
    print(n)
    n+=1



#   4)  Simulación de un do-while

n = 1
while True:
    print(n)
    if(n==10):
        break
    n+=1