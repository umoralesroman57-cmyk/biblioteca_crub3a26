class Carrera:

    # Constructor
    
    def _init_(self, id, nombre):
        self.id = id
        self.nombre = nombre
        
    def mostrar_info(self):
        return f"Carrera ID: {self.id}, Nombre: {self.nombre}"