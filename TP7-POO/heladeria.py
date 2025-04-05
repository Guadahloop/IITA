from restaurante import Restaurante

class Heladeria(Restaurante):
    def __init__(self, restaurante_nombre, sabores):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = "Helados"
        self.sabores = sabores

    def mostrar_sabores(self):
        print(f"Sabores disponibles: {self.sabores}")