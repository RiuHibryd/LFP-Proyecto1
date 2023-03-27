from Abstract.abstract import Expression

class Errores(Expression):
    
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)
        
    def operar(self , no):
        no1 = f'\t\t"No.": {no}\n' #No. de error
        descripcion = '\t\t"Descripcion-Token": {\n' #Descripcion del error
        lexema = f'\t\t\t"KLexema": {self.lexema}\n' #Lexema del error
        tipo = '\t\t\t"Tipo:": Error Lexico\n' #Tipo de error
        fila = f'\t\t\t"Fila": {self.fila}\n' #Fila del error
        columna= f'\t\t\t"Columna": {self.columna}\n' #Columna del error
        fin = '\t\t}\n' #Fin de la descripcion

        return '\t{\n' + no1 + descripcion + lexema + tipo + fila + columna + fin + '\t}'
    
    def getFila(self): #Metodo para obtener la fila
        return super().getFila()
    
    def getColumna(self): #Metodo para obtener la columna
        return super().getColumna()