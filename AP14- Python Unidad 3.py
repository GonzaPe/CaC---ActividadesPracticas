""" class persona:
    def inicializar(self, nombre):
        self.nombre = nombre
    def imprimir(self):
        print("Nombre: {}".format(self.nombre))

persona1 = persona() #defino a persona1 como un objeto perteneciente a la clase persona
persona2 = persona()

persona1.inicializar("Pedro") #llamo al método (función) inicializar que toma el parámetro entre paréntesis como nombre
persona1.imprimir() #imprimo los valores de las variables

persona2.inicializar("Carla")
persona2.imprimir() """

#1) 15:38 Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” y “print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos por consola.
""" class Persona:
    def __init__(self, set_nombre, set_edad):
        self.nombre = set_nombre
        self.edad = set_edad
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def print_persona(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))

persona1 = Persona("Pedro", 89) #defino a persona1 como un objeto perteneciente a la clase persona que toma el parámetro entre paréntesis como nombre
persona1.print_persona() #imprimo los valores de las variables

persona2 = Persona("Juan Pelotaz", 44)
print(f"El señor {persona2.get_nombre()} tiene {persona2.get_edad()} años") """

# 2)  Agregarle a la clase anterior un constructor que reciba nombre y edad. 
""" class Persona:
    def __init__(self, set_nombre, set_edad): #acá está el constructor por lo que no cambia respecto a lo hecho en el caso 1
        self.nombre = set_nombre
        self.edad = set_edad
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def print_persona(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad)) """

#3)  Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva True o False. 
""" class Persona:
    def __init__(self, set_nombre, set_edad):
        self.nombre = set_nombre
        self.edad = set_edad
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def es_mayor_de_edad(self):
        if self.edad>=18:
            return True
        else:
            return False
    def print_persona(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))

persona1 = Persona("Hector Pelotaz", 17)
print(f"Es mayor de edad? {persona1.es_mayor_de_edad()}") """

#4)  Agregarle un método “es_mayor_que” el cual recibe un objeto persona y compara su edad con la del objeto actual.
""" class Persona:
    def __init__(self, set_nombre, set_edad):
        self.nombre = str(set_nombre)
        self.edad = int(set_edad)
    
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def es_mayor_de_edad(self):
        if self.edad>=18:
            return True
        else:
            return False
    
    def es_mayor_que(self, personaX):
        if self.edad>personaX.get_edad():
            return True
        else:
            return False
    def print_persona(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))

persona1 = Persona("Juan", 20)
persona2 = Persona("Carlos", 29)
print(persona1.es_mayor_que(persona2)) """

#5) Agregarle un método estático “get_mayor” que reciba dos objetos Persona y devuelva el de edad mayor. 
""" class Persona:
    def __init__(self, set_nombre, set_edad):
        self.nombre = str(set_nombre)
        self.edad = int(set_edad)
    
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def es_mayor_de_edad(self):
        if self.edad>=18:
            return True
        else:
            return False
    
    def es_mayor_que(self, personaX):
        if self.edad>personaX.get_edad():
            return True
        else:
            return False
    
    @staticmethod
    def get_mayor(personaX, personaY):
        if Persona.get_edad(personaX)>Persona.get_edad(personaY):
            return personaX.nombre
        else:
            return personaY.nombre
    
    def print_persona(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))

persona1 = Persona("Juan", 20)
persona2 = Persona("Carlos", 29)

print(Persona.get_mayor(persona1, persona2)) """

#6)  Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.´

""" class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
    
    def aprobado(self):
        if self.nota>6:
            print("Aprobado")
        else:
            print("Desaprobado")

alumno1 = Alumno("Juan", 8)
alumno1.imprimir()
alumno1.aprobado() """

#7)  Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno). 

#8)  Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

#9)  Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones: Añadir contacto, Listar contactos, Buscar contacto, Editar contacto, Cerrar agenda.

#10) En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado. Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total. La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total. 

