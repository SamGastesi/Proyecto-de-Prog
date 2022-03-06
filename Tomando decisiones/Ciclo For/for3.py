# Ejercicio de for

positivos = 0; negativos = 0; neutros = 0

for i in range(6):
    num = int(input('Ingrese un número: '))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        neutros += 1

print('Total de positivos:', positivos)
print('Total de negativos:', negativos)
print('Total de neutros:', neutros)
