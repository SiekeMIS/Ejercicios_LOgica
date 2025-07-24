# """
# Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para 
# inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no. (1)
# """
# class Estudiante:
# 	def __init__(self, nombre, nota):
# 		self.nombre = nombre
# 		self.nota = nota

# 	def imprimir(self):
# 		print(f"Nombre Estudiante:\n{self.nombre}\nNota Estudiante:\n{self.nota}")

# 	def resultado(self):
# 		if self.nota >= 4:
# 			return f"El alumno {self.nombre} ha aprobado con un {self.nota}"
# 		else:
# 			return f"El alumno {self.nombre} ha reprobado con un {self.nota}"
		
# # Ejemplo de uso
# if __name__ == "__main__":
# 	Estudiante_1 = Estudiante("Lucas Darrouy", 5.0)
# 	Estudiante_1.imprimir()
# 	print(Estudiante_1.resultado())

# """
# Crea una clase “Persona”. Con atributos nombre y edad. Además, hay que crear un método “cumpleaños”, que aumente en 1 la edad de la persona cuando se invoque sobre un objeto creado con “Persona”.
# Tendríamos que lograr ejecutar el siguiente código con la clase creada: (2)
# """

# class Persona:
# 	def __init__(self, nombre, edad):
# 		self.nombre = nombre
# 		self.edad = edad
	
# 	def cumpleaños(self):
# 		self.edad += 1

# p = Persona(input("Ingrese su nombre:\n"), int(input("Ingrese su edad:\n")))
# p.cumpleaños()
# p.cumpleaños()
# print(f"{p.nombre} {p.edad}")

# """
# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. 
# Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora. (3)
# """
# class Calculadora:
# 	def __init__(self, numero_uno, numero_dos):
# 		self.numero_uno = numero_uno
# 		self.numero_dos = numero_dos
	
# 	def suma(self):
# 		resultado = self.numero_uno + self.numero_dos
# 		print (f"La suma de los números {self.numero_uno} + {self.numero_dos} es: {resultado}")

# 	def resta(self):
# 		resultado = self.numero_uno - self.numero_dos
# 		print(f"La resta de los números {self.numero_uno} - {self.numero_dos} es: {resultado}")
	
# 	def multiplicación(self):
# 		resultado = self.numero_uno * self.numero_dos
# 		print(f"El producto de los numeros {self.numero_uno} * {self.numero_dos} es: {resultado}")
	
# 	def división(self):
# 		resultado = self.numero_uno / self.numero_dos
# 		print(f"La división de los numero {self.numero_uno} / {self.numero_dos} es: {resultado}")

# # Ejemplo de uso:
# calculo = Calculadora(5, 12)
# calculo.suma()

# calculo = Calculadora(1, 15)
# calculo.resta()

# calculo = Calculadora(12, 2)
# calculo.multiplicación()

# calculo = Calculadora(10, 2)
# calculo.división()


# Crear una clase “Persona” que sea la clase padre de otra clase “Estudiante”. Por tanto:
# En la clase “Persona” su método __init__() debe de estar preparado para recibir nombre y apellido. Además, esta clase , debe tener un método para mostrar nombre_completo() 
# el cual debe mostrar el nombre acompañado del apellido.
# La otra clase “Estudiante”, debe de poder heredar de “Persona”, y además recibir los argumentos nombre y edad. También la clase “Estudiante”, recibe el valor 
# “carrera”, y además contar con un método mostrar_carrera(). Las dos clases son obligatorias. (4)

# class Persona():
#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.apellido = apellido

#     def nombre_apellido(self):  # Falta el parámetro self
#         print(self.nombre + " " + self.apellido)  # Agregué espacio entre nombre y apellido

# class Estudiente(Persona):  # Hay un typo en "Estudiente" (debería ser "Estudiante")
#     def __init__(self, nombre, apellido, edad, carrera):  # Typo en "apellido" (debería ser "apellido")
#         super().__init__(nombre, apellido)  # Typo en "apellido"
#         self.edad = edad
#         self.carrera = carrera

#     def mostrar_carrera(self):  # Falta el parámetro self
#         print(self.carrera)  # Debería mostrar self.carrera en lugar de redefinir la variable

# joven_estudiante = Estudiente("Lucas", "Rosas", 20, "Psicologia")
# print(joven_estudiante.nombre)
# print(joven_estudiante.apellido)  # Typo en "apellido"
# print(joven_estudiante.edad)
# print(joven_estudiante.carrera)