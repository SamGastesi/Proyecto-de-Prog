# Ejercicio de continue

f = 0
for i in range(10):
    f += 2
    print("i:",i,"f:",f)
    if f >= 2 and  f <= 18:
        continue
    print("El valor de f:",f)
