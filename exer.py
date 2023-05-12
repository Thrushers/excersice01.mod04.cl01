class Animal():
    def __init__(self,nombre,raza,edad,peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        
animal01 = Animal("Zeus","Pura sangre",5, 450)

animal02 = Animal("Boulder","Atlas",10,130)

print(f"Animal nombre: {animal01.nombre}, Raza: {animal01.raza}, Edad: {animal01.edad}")

print(f"Animal nombre: {animal02.nombre}, Raza: {animal02.raza}, Edad: {animal02.edad}")