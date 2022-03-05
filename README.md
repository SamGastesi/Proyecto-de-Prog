# PORTAFOLIO DE FUNDAMENTOS-DE-PROGRAMACION
# Qué es Python?
Es un lenguaje de programación de alto nivel apto para desarrollar todo tipo de apps, un ejemplo de estas seria para desarrollo web y aplicaciones informáticas, es sencillo de aprender ya que es parecido al lenguaje humano; utiliza un lenguaje interpretado que se ejecuta directamente por el ordenador y no necesita traducirse a lenguaje de máquina.
Python nos brinda todas las herramientas necesarias para desarrollar futuros proyectos que nos planteemos todo esto gratuitamente, por lo tanto, es una opción multiplataforma, bastante interesante para los desarrolladores que no quieren preocuparse por pagar altos costos de desarrollo.
# Qué es una variable?
Una variable es un nombre que se refiere a un valor. La sentencia de asignación crea nuevas variables y les da valores. Cuando escribimos código, las variables se utilizan para:
* Guardar datos y estados.
* Asignar valores de una variable a otra.
* Representar valores dentro de una expresión matemática.
* Mostrar valores por pantalla.
## Nombrando una variable
``` Python
variable =
# aquí en “variable” es donde se guardará la información y en “=” se le asigna un dato o valor a la variable.
```
## Asignando valores a una variable 
``` Python
variable = 45
variable = ¡Hola mundo!
# aquí el “=” asigna un valor numérico (45) en la primera variable y en la segunda un mensaje de bienvenida (¡Hola mundo!)
```
## Operadores básicos
* Suma: +
* Resta: -
* Multiplicación: *
* División: /
* Potenciación: **
* División entera: //
* Modulo: %
### Suma
```Python
# Colocamos dos variables con sus respectivos valores
x = 8
y = 4
# debemos crear una variable en donde se guarde el resultado de la operación, en este caso la suma
result = 0
# escribimos las variables situando en medio de ellos el signo ‘+’
result = (x + y)
result = 12
# y por último escribimos la función print para que muestre el resultado exacto
print(result)
```
### Resta
```Python
# Colocamos dos variables con sus respectivos valores
x = 50
y = 15
# debemos crear una variable en donde se guarde el resultado de la operación, en este caso la resta
result = 0
# escribimos las variables situando en medio de ellos el signo ‘-’
result = (x - y)
result = 35
# y por último escribimos la función print para que muestre el resultado exacto
print(result)
```
### Multiplicación
```Python
# Colocamos dos variables con sus respectivos valores
x = 10
y = 5
# debemos crear una variable en donde se guarde el resultado de la operación, en este caso la multiplicación 
result = 0
# escribimos las variables situando en medio de ellos el signo ‘*’
result = (x * y)
result = 50
# y por último escribimos la función print para que muestre el resultado exacto
print(result)
```
### División
```Python
# Colocamos dos variables con sus respectivos valores
x = 45
y = 3
# debemos crear una variable en donde se guarde el resultado de la operación, en este caso la división 
result = 0
# escribimos las variables situando en medio de ellos el signo ‘/’
result = (x / y)
result = 15
# y por último escribimos la función print para que muestre el resultado exacto
print(result)
```
### Módulo
```Python
# Colocamos dos variables con sus respectivos valores
x = 20
y = 8
# debemos crear una variable en donde se guarde el resultado de la operación, en este caso la división 
result = 0
# escribimos las variables situando en medio de ellos el signo ‘%’
result = (x % y)
result = 4
# y por último escribimos la función print para que muestre el resultado exacto
print(result)
```
### Potencia
```Python
# Colocamos dos variables con sus respectivos valores
x = 2
y = 3
# debemos crear una variable en donde se guarde el resultado de la operación, en este caso la división 
result = 0
# escribimos las variables situando en medio de ellos el signo ‘**’
result = (x ** y)
result = 8
# y por último escribimos la función print para que muestre el resultado exacto
print(result)
```
# Tipos de datos en Python
## Integer
Hace referencia a los números enteros ya sean positivos o negativos, no se admiten los decimales. En Python mayormente lo usamos como int, este nos permite almacenar un valor numérico con las características antes dadas, y no debemos preocuparnos del tamaño del número almacenado.
```Python
X = 65
Y = -34
Z = 24675322
```
## Float
El tipo numérico ‘float’ nos permite representar un numero decimal ya sea este positivo o negativo.
```Python
num = 73.895
print(type(num)) 
#nos muestra el tipo de dato que representa
```
## String
Lo utilizamos para almacenar secuencias de carácteres, lo hacemos mediante las dobles comillas "" para crear un texto de esta característica.
```Python
mes = "noviembre"
print(type(mes)) 
#nos muestra el tipo de dato que representa
```
## Casting en Python
Este dato nos da la posibilidad de cambiar un tipo de dato a otro. Tales como int, string o float.
```Python
   float a int: int (7.4)
   str a int: int ("938")
   int a str: str(95)
  ```
## List
Aquí podemos almacenar cualquier tipo de información, en ellas puedes guardar prácticamente lo que quieras, lo hacemos mediante los corchetes [] y separados por una coma (,).
```Python
list = [ 15,10,5,1,["quince","diez","cinco","uno"]]
print(list)
```
## Tuple
Es una estructura de datos donde podemos guardar información heterogénea y homogénea, son inmutables, es decir, que después de ser creado no puede cambiarse, los podemos presentar mediante paréntesis () o separados por una coma.
```Python
tupla = 10, 50, 20
print(tupla)

tupla = (10, 50, 20)
print(type(tupla)) 
print(tupla)
```
## Dictionary
Son una serie de datos que podemos almacenar definiendo una llave (key) y un valor (value). Son creados mediante un par de corchetes y separados por una coma. Una ventaja de esto es que podemos acceder a todos los valores almacenados usando simplemente las claves.
```Python
d5 = {
  "Nombre": "Samantha",
  "Edad": 18,
  "Documento": 4839564
}
print(d5)
```

# Tomando decisiones
## Sentencia if
Esta palabra utilizada en Python significa “si” y la utilizamos cuando una tenemos una expresión que necesitamos evaluar y ver si el resultado es verdadero, si es así se ejecutará por lo contrario seguirá con el próximo bloque para determinar su valor. 
```Python
# Escriba un programa que solicite un valor entero al usuario
# Determine si es par o impar

num = int(input("Ingrese un número:"))

if (num%2==0):
    print("El número es par",)
    print(num,"Es par")
else:
    print("El número es impar")  
```   
## Ciclo For
Es un bucle que repite el bloque de instrucciones un número prederminado de veces. El bloque de instrucciones que se repite se suele llamar cuerpo del bucle y cada repetición se suele llamar iteración.El cuerpo del bucle se ejecuta tantas veces como elementos tenga el elemento recorrible.
```Python
# Calcula la suma y la media aritmética de N números reales. 
# Solicitar el valor de n al usuario y cada uno de los N números reales.

n = int(input("Ingrese números a su elección: "))
suma= 0
for i in range(n):
    nota =int(input('Ingrese el número' + str (i+1) +  ':'))
    suma += nota
    
promedio = suma/n 
print("promedio:", promedio)
```
## Ciclo While
El ciclo while evalúa una condición y luego ejecuta un bloque de código si la condición es verdadera. El bloque de código se ejecuta consecutivamente hasta que la condición llega a ser falsa.
```Python
# 10 - 20

num = 11

while num < 10 or num > 20 or num%2!= 0:
    num = int(input("Ingrese número:"))

print("Se fue")
```
## Break
La instrucción break le proporciona la oportunidad de cerrar un bucle cuando se activa una condición externa. Debe poner la instrucción break dentro del bloque de código bajo la instrucción de su bucle, generalmente después de una instrucción if condicional.
```Python
j = 0
for i in range (10):
    j += 2
    print ("i;", i, "j:", j)
    if j == 10:
        break
```
## Continue
Sirve para detener la iteración actual y volver al principio del bucle para realizar otra iteración, si corresponde.
```Python
contador = 0
for i in range (10):
    for j in range (10):
        contador += 1
        print ("i:", i, "j:", j)
        if contador > 50:
            continue
print ("contador:", contador)
```
