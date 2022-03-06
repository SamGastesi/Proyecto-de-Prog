# Ejercicio de if

a = (70 - 95)
b = 80
c = 90

if a >= 70:
    print("continuemos")
    if b == 70:
        print("incorrecto")
    elif b == 80:
        print("continuemos")
        if c > 90:
            print("incorrecto")
        elif c > 70:
            print("Las condiciones son correctas")
elif a < 70:
    print("Las condiciones son incorrectas")
