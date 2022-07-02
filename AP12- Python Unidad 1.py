#1) 8:06
""" print("Hello World")  """

#2) 8:07
""" print(3+5) """

#3) 8:08
""" nombreUsuario = input("Por favor ingrese su nombre de usuario: ")
print(f"Hola {nombreUsuario}")
 """

#4) 8:10
""" n1 = int(input("Ingrese un primer número para sumar: "))
n2 = int(input("Ingrese un segundo número para sumar: "))
suma = n1 + n2
print(suma) """

#5) 8:15
""" n1 = int(input("Ingrese un primer número: "))
n2 = int(input("Ingrese un segundo número: "))
if n1>n2:
    print(f"El mayor es {n1}")
elif n1<n2:
    print(f"El mayor es {n2}")
else:
    print("Ambos números son iguales") """

#6) 8:19
""" n1 = int(input("Ingrese un primer número: "))
n2 = int(input("Ingrese un segundo número: "))
n3 = int(input("Ingrese un tercer número: "))

if n1>n2:
    if n1>n3:
        print(f"El mayor es {n1}")
    elif n1<n3:
        print(f"El mayor es {n3}")
    else:
        print(f"Ambos números ({n3}) son iguales y mayores")
elif n2>n1:
    if n2>n3:
        print(f"El mayor es {n2}")
    elif n2<n3:
        print(f"El mayor es {n3}")
    else:
        print(f"Ambos números ({n3}) son iguales y mayores")
else:
    if n2>n3:
        print(f"Los números mayores son los {n2}")
    elif n2<n3:
        print(f"El mayor es {n3}")
    else:
        print(f"Todos los números ({n3}) son iguales") """

#7) 8:37
""" n1 = int(input("Ingrese un número para saber si es divisible por 2: "))
if n1%2==0:
    print("El número ingresado es par")
else:
    print("El número ingresado no es par") """

#8) 8:39
""" n1 = int(input("Ingrese un número para saber si es divisible por 2, 3, 5 o 7: "))
if n1%2==0:
    print("El número ingresado es divisible por 2")
elif n1%3==0:
    print("El número ingresado es divisible por 3")
elif n1%5==0:
    print("El número ingresado es divisible por 5")
elif n1%7==0:
    print("El número ingresado es divisible por 7")
else:
    print("El número ingresado no es divisible por 2, 3, 5 o 7")
 """
#9) 8:49
""" n1 = int(input("Ingrese un número para saber si es divisible por 2, 3, 5 o 7: "))
divisible = [2, 3, 5, 7]
divisores = []
for i in divisible:
    if n1%i==0:
        divisores.append(i)
if len(divisores)==0:
    print(f"{n1} no es divisible por ninguno de los cuatro números.")
else:
    print(f"{n1} es divisible por {divisores}.") """

#10) 9:17
""" n1 = int(input("Ingrese un número para saber por cuales es divisible: "))
divisores = []

for i in range(1, int(n1/2)):
    if n1%i==0:
        divisores.append(i)
print(f"{n1} es divisible por {divisores}") """

#11) 9:22

""" n1 = int(input("Ingrese un número para saber si es un número primo: "))
divisores = []

for i in range(2, int(n1/2)):
    if n1%i==0:
        divisores.append(i)

if len(divisores)==0:
    print(f"{n1} es un número primo.")
else:
    print(f"{n1} no es un número primo.") """

#12) 9:29
""" from cgitb import text


nota = int(input("Ingrese la nota: "))

if nota>=0 and nota<3:
    print("Muy deficiente")
elif nota>=3 and nota<5:
    print("Insuficiente")
elif nota>=5 and nota<6:
    print("Suficiente")
elif nota>=6 and nota<7:
    print("Bien")
elif nota>=7 and nota<9:
    print("Notable")
elif nota>=9 and nota<=10:
    print("Sobresaliente")
else:
    print("No ha ingresado un valor válido.") """

#13) 9:36
""" limite = int(input("Ingrese el valor límite de la pirámide: "))
for i in range(1, limite+1):
    numText = str(i)
    texto = numText*i
    print(texto)
 """
#14) 9:42
""" limite = int(input("Ingrese el valor límite de la pirámide: "))
for i in range(limite, 0, -1):
    numText = str(i)
    texto = numText*i
    print(texto) """

#15) 9:52 (hubo un llamado de la oficina)
numLimit = int(input("Ingrese el valor límite: "))
for i in range(1, numLimit+1):
    texto = ""
    if i%4==0 and i%5==0 and i%9==0:
        print(f"{i} (Múltiplo de 4 y 9)")
        print("------------------------------------------------------------")
    elif i%4==0 and i%5==0:
        print(f"{i} (Múltiplo de 4)")
        print("------------------------------------------------------------")
    elif i%9==0 and i%5==0:
        print(f"{i} (Múltiplo de 9)")
        print("------------------------------------------------------------")
    elif i%4==0 and i%9==0:
        print(f"{i} (Múltiplo de 4 y 9)")
    elif i%4==0:
        print(f"{i} (Múltiplo de 4)")
    elif i%5==0:
        print(i)
        print("------------------------------------------------------------")
    elif i%9==0:
        print(f"{i} (Múltiplo de 9)")
    else:
        print(i)
#10:07