from abc import ABC, abstractmethod

class Expression(ABC):
    # Clase abstracta para las expresiones matemáticas
    
    def __init__(self, fila, columna):
        # Constructor que inicializa la fila y columna donde aparece la expresión
        self.fila = fila
        self.columna = columna
        
    @abstractmethod
    def operar(self, arbol):
        # Método abstracto que opera la expresión dada una tabla de símbolos
        pass
    
    @abstractmethod
    def getFila(self):
        # Método abstracto que devuelve la fila donde aparece la expresión
        return self.fila
    
    @abstractmethod
    def getColumna(self):
        # Método abstracto que devuelve la columna donde aparece la expresión
        return self.columna