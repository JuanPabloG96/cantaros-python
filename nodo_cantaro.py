class NodoCantaro:
    def __init__(self, estado, operacion, padre=None):
        self.estado = estado
        self.operacion = operacion
        self.padre = padre
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)