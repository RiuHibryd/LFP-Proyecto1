from Abstract.abstract import Expression
from math import *

class Trigonometricas(Expression):
    
    def __init__(self, left, tipo, fila, columna):
        self.left = left
        self.tipo = tipo
        super().__init__(fila, columna)
        
    def operar(self, arbol):
        leftValue = ''
        if self.left != None:
            leftValue = self.left.operar(arbol)   # Obtiene el valor de la expresión que está a la izquierda del operador
        if self.tipo.operar(arbol) == 'Seno': # Si el operador es un seno
            return sin(leftValue)
        elif self.tipo.operar(arbol) == 'Coseno': # Si el operador es un coseno
            return cos(leftValue)
        elif self.tipo.operar(arbol) == 'Tangente': # Si el operador es una tangente
            return tan(leftValue)
        else:
            return None    
    
    def getFila(self):
        return super().getFila() # Obtiene la fila de la clase padre
    
    def getColumna(self):
        return super().getColumna() # Devuelve la columna donde se encuentra la expresión