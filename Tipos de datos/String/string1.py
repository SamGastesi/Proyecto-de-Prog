# Ejercicio de string

dog = input("Ingrese una cadena: ")
while True:
    dog = input("Ingrese un carácter: ")
    if len(dog) == 1: break

print("En la cadena",dog,"aparecen",dog.count(dog),"veces el carácter",dog)
