# """
# Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para 
# inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
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
# Tendríamos que lograr ejecutar el siguiente código con la clase creada:
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