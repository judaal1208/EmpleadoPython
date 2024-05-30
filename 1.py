class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")

class Salario:
    def __init__(self):
        self.salario = float(input("Ingrese el salario del empleado: "))

class Designacion(Empleado, Salario):
    def __init__(self):
        Empleado.__init__(self)
        Salario.__init__(self)

    def designar_cargo(self, cargo):
        self.cargo = cargo

# Verificación del código
objeto_designacion = Designacion()
print("Nombre del empleado:", objeto_designacion.nombre,'Salario del empleado:', objeto_designacion.salario)
print("¿El objeto tiene el método 'nombre'? ", hasattr(objeto_designacion, 'nombre'))
print("¿El objeto tiene el método 'salario'? ", hasattr(objeto_designacion, 'salario'))
