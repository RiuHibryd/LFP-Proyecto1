from Abstract.abstract import Expression

class Aritmeticas(Expression):
    
    def __init__(self, left, right, tipo, fila, columna):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, columna)
        

    
    def operar(self, arbol):    #Operar
        leftValue = ''
        rightValue = ''
        if self.left != None:   #Si el nodo izquierdo no es nulo
            leftValue = self.left.operar(arbol)   #Se obtiene el valor del nodo izquierdo
        if self.right != None:  #Si el nodo derecho no es nulo
            rightValue = self.right.operar(arbol) #Se obtiene el valor del nodo derecho
    
        if self.tipo.operar(arbol) == 'Suma': #Si el tipo de operacion es suma
            return leftValue + rightValue #Se retorna la suma de los valores
        elif self.tipo.operar(arbol)  == 'Resta': #Si el tipo de operacion es resta
            return leftValue - rightValue # Se retorna la resta de los valores
        elif self.tipo.operar(arbol)  == 'Multiplicacion': #Si el tipo de operacion es multiplicacion
            return leftValue * rightValue # Se retorna la multiplicacion de los valores
        elif self.tipo.operar(arbol)  == 'Division': #Si el tipo de operacion es division
            return leftValue / rightValue # Se retorna la division de los valores
        elif self.tipo.operar(arbol)  == 'Modulo': #Si el tipo de operacion es modulo
            return leftValue % rightValue # Se retorna el modulo de los valores
        elif self.tipo.operar(arbol)  == 'Potencia': #Si el tipo de operacion es potencia
            return leftValue ** rightValue # Se retorna la potencia de los valores
        elif self.tipo.operar(arbol)  == 'Raiz': #Si el tipo de operacion es raiz
            return leftValue ** (1/rightValue) # Se retorna la raiz de los valores
        elif self.tipo.operar(arbol)  == 'Inverso': #Si el tipo de operacion es inverso
            return 1/leftValue # Se retorna el inverso de los valores
        else: 
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()