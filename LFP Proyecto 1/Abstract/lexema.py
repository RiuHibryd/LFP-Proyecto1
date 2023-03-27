from Abstract.abstract import Expression
# Clase Lexema que hereda de la clase abstracta Expression
class Lexema(Expression):
    
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema # guarda el lexema
        super().__init__(fila, columna)
        
    def operar(self, arbol):
        return self.lexema # retorna el valor del lexema
    
    
    def getFila(self):
        return super().getFila()  # retorna la fila del lexema
    
    def getColumna(self):
        return super().getColumna()  # retorna la columna del lexema