#1) 10:00
""" def mayor(n1, n2, n3):
    if n1>n2:
        if n1>n3:
            return n1
        elif n1<n3:
            return n3
        else:
            return -1
    elif n2>n1:
        if n2>n3:
            return n2
        elif n2<n3:
            return n3
        else:
            return -1
    else:
        if n2>n3:
            return n2
        elif n2<n3:
            return n3
        else:
            return -1

def programa():
    n1 = int(input("Ingrese un primer número: "))
    n2 = int(input("Ingrese un segundo número: "))
    n3 = int(input("Ingrese un tercer número: "))
    
    numMayor = mayor(n1, n2, n3)
    if numMayor==-1:
        return "No existe un número estrictamente mayor"
    else:
        return numMayor

print(programa()) """

#1) 10:24

def programa():
    bisiesto=False
    anoValido=False
    mesValido=False
    diaValido=False
    mesDe31 = [1, 3, 5, 7, 8, 10, 12]
    while anoValido==False:
        ano = int(input("Ingrese el año: "))
        if ano>=0:
            if ano%4==0:
                if ano%100==0:
                    if ano%400==0:
                        bisiesto=True
                bisiesto=True
            anoValido=True
        else:
            print("Ingrese un año válido (positivo)")
    while mesValido==False:
        mes = int(input("Ingrese el mes: "))
        if mes>0 and mes<13:
            mesValido=True
        else:
            print("Ingrese un mes válido (entre 1 y 12)")
    while diaValido==False:
        dia = int(input("Ingrese el día: "))
        if dia>0 and dia<32:
            if mes==2:
                if dia<=28 or (dia==29 and bisiesto==True):
                    diaValido=True
                else:
                    print("Ingrese un día válido (considere que es febrero)")
            elif dia<31:
                diaValido=True
            elif mes in mesDe31 and dia==31:
                diaValido=True
            else:
                print("Ingrese un día válido (considere la duración del mes)")
        else:
            print("Ingrese un día válido (considere la duración de los meses)")

programa()

#3) 12:00
def vuelto():
    precio = int(input("Ingrese el total a cobrar: "))
    abono = int(input("Ingrese el total abonado: "))
    
    if abono<precio