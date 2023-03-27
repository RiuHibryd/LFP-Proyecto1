from Abstract.abstract import Expression

class Numero(Expression):
    
    def __init__(self, valor, fila, columna):
        self.valor = valor  # Almacena el valor numérico
        super().__init__(fila, columna)  # Inicializa la clase padre

    def operar(self, arbol):
        return self.valor  # Devuelve el valor almacenado
    
    def getFila(self):
        return super().getFila()  # Obtiene la fila de la clase padre
    
    def getColumna(self):
        return super().getColumna()   # Obtiene la columna de la clase padre