# Ejercicio de while

d = 0
n  = int(input("Número (0 para terminar): "))
while n != 0:
    if n > 0:
        d += 1
    n = int(input("Número (0 para terminar): ")) 
    
print("Cantidad de positivos:", d)
