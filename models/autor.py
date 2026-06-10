class Autor:

    # Constructor
    
    def _init_(self, id, nombre):
        self.id = id
        self.nombre = nombre
        
    def mostrar_info(self):
        return f"Autor ID: {self.id}, Nombre: {self.nombre}"