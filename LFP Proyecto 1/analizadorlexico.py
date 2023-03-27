from Instrucciones.aritmeticas import *
from Instrucciones.trigonometricas import *
from Instrucciones.Errores import *
from Abstract.lexema import *
from Abstract.numero import *


#Este es un listado de palabras reservadas como lo son multiplicacion y asi, RTEXTO es un token
reserved = { 
    'OPERACION'         : 'Operacion',
    'RVALOR1'            : 'Valor1',
    'RVALOR2'           : 'Valor2',
    'RSUMA'             : 'Suma',
    'RMULTIPLICACION'   : 'Multiplicacion', 
    'RDIVISION'         : 'Division',
    'RPOTENCIA'         : 'Potencia',
    'RRAIZ'             : 'Raiz',   
    'RINVERSO'          : 'Inverso',
    'RSENO'             : 'Seno',
    'RCOSENO'           : 'Coseno',
    'RTANGENTE'         : 'Tangente',
    'RMODULO'           : 'Modulo',
    'RTEXTO'            : 'Texto',
    'RCOLORFONDONODO'   : 'Color-Fondo-Nodo',
    'RCOLORFUENTENODO'  : 'Color-Fuente-Nodo',
    'RFORMANODO'        : 'Forma-Nodo',  
    'COMA'              : ',',
    'PUNTO'             : '.',
    'DPUNTO'            : ':',
    'CORI'              : '[',
    'CORD'              : ']',
    'LLAVEI'            : '{',
    'LLAVED'            : '}',
}

#Convertimos el diccionario de arriba en una lista con el nombre lexemas

lexemas = list(reserved.values())

#Llevamos la lsita de lineas, columnas, instrucciones y lista_lexemas
global n_lineas
global n_columnas   
global instrucciones
global lista_lexemas
global lista_errores

n_lineas = 1
n_columnas = 1
lista_lexemas = []
instrucciones = []
lista_errores = []

#Metodo que recibe una cadea donde mando a llamar a mi liena y columna

def instruccion(cadena):
    global n_lineas
    global n_columnas
    global lista_lexemas
    
#Aqui armamos el lexema donde se ejecuta caracter por caracter donde se va eliminado y se haga mas pequeña eso es posible con el puntero
    lexema = ''
    puntero = 0
    
    while cadena:       #Mientras alla algo nos enciclamos 
        char = cadena[puntero]     #El char sera la posicion cero en la cadena
        puntero += 1
        
        if char == '\"':            #Si el char es igual a las comillas vamos a empezar armar nuestro lexema 
            lexema, cadena = armar_lexema(cadena[puntero:])    #Colocamos cadena aqui para que se actualice la cadena que esta en el while y no se me encicle
            if lexema and cadena:   #Esto quiere decir que si cadena no me retorno nulo se sumara uno a la cadena
                n_columnas +=1
                
                l = Lexema(lexema, n_lineas, n_columnas) 
                
                lista_lexemas.append(l)    #Aqui armamos lexema como clase
                n_columnas += len(lexema) +1  
                puntero = 0        #Reiniciamos porque la cadena recibida fue actualizada
        elif char.isdigit():        #Si es un numero mandaremos a traer la cadena
            token, cadena = armar_numero(cadena) #Mandamos la cedena como tal para no cortar nada
            if token and cadena:
                n_columnas +=1
                
                n = Numero(token, n_lineas, n_columnas)
                
                lista_lexemas.append(n)
                n_columnas += len(str(n)) +1    #El toquen lo convertimos en un string y despues a cadena
                puntero = 0
                
        elif char == '[' or char == ']':        #Si el char es igual a un corchete que cierra o abre 
            
            c = Lexema(char, n_lineas, n_columnas)
            
            lista_lexemas.append(c)
            cadena = cadena[1:]
            n_columnas +=1
            puntero = 0
        elif char == '\t':        #En este if ingnoramos los saltos de linea
            n_columnas +=4
            cadena = cadena[4:]       #Cortamos la cadena con esos espacions
            puntero = 0              #Reiniciamos el puntero
        elif char == '\n':        #Este if es por si el char es un salto de linea       
            cadena = cadena[1:]
            puntero = 0
            n_lineas += 1
            n_columnas = 1
        elif char == ':' or char == ',' or char == '.' or char == '}' or char == '{' or char == '\r' or char == ' ': #Esto nos ayuda por si en dado caso viene uno de esos signos y reconocerlos 
            n_columnas += 1
            cadena = cadena[1:]
            puntero = 0
        else: 
            lista_errores.append(Errores(char, n_lineas, n_columnas)) #Estos crea la lista de errores en dado caso la letras no es renocible y asi genera los errores
            cadena = cadena[1:]
            puntero = 0
            n_columnas += 1

    return lista_lexemas

#metodo armar lexema
def armar_lexema(cadena):
    global n_lineas
    global n_columnas
    global lista_lexemas
    lexema = ''
    puntero = ''
    for char in cadena:    #Aqui recorremos nuestra cadena 
        puntero += char
        if char == '\"':         #Ya leimos la comilla 
            return lexema, cadena[len(puntero):]
        else:
            lexema += char
    return None, None #Para que no falle se retorna None None


#Metodo para armar los numeros y sus operaciones
def armar_numero(cadena):
    numero = ''
    puntero = ''
    is_decimal = False      #Numeros decimales
    for char in cadena:
        puntero += char
        if char == '.':
            is_decimal = True 
        if char == '"' or char == ' ' or char == '\n' or char == '\t' or char== ']' or char== "}]":   #Por si viene una comia, un espacio, una tabulacion o salto de linea
            if is_decimal:
                return float(numero), cadena[len(puntero)-1:]
            else:
                return int(numero), cadena[len(puntero)-1:]
        else:
            numero += char
    return None, None

def operar():
    global lista_lexemas
    global instrucciones
    operacion = ''
    n1 = ''
    n2 = ''
    while lista_lexemas:                            
        lexema = lista_lexemas.pop(0)       
        if lexema.operar(None) == 'Operacion':  
            if lista_lexemas:       
                operacion = lista_lexemas.pop(0)
        elif lexema.operar(None) == 'Valor1':
            n1 = lista_lexemas.pop(0)
            if n1.operar(None) == '[':
                n1 = operar()
        elif lexema.operar(None) == 'Valor2':
            n2 = lista_lexemas.pop(0)
            if n2.operar(None) == '[':
                n2 = operar()
        #Aqui ya armamos la funcion aritmetica y nos recibe lado dercho e izquierdo osea fila y columna
        if operacion and n1 and n2:
            return Aritmeticas(n1, n2, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n2.getFila()}:{n2.getColumna()}') 

        elif operacion and n1 and operacion.operar(None) == ('Seno' or 'Coseno' or 'Tangente'):
            return Trigonometricas(n1, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
    return None

#Aqui creamos su metodo recursivo

def operar2():
    global instrucciones
    while True:
        operacion = operar()
        if operacion:
            instrucciones.append(operacion)
        else:
            break
        
    #for instruccion in instrucciones:
        #print(instruccion.operar())
    return instrucciones
        

def getErrores():
    global lista_errores
    return lista_errores

    
def grafica(self):
        vacio= ''
        titulo,fondo,fuente,forma = vacio,vacio,vacio,vacio
        posicion =0

        for atributo in self.atributo_lista:
            atri = atributo.verificar()

            if atri[posicion] == '"texto"':
                titulo = atri[1]
                print(titulo)
            elif atri[posicion] == '"color_fondo"':
                fondo = atri[1]
                print(fondo)
            elif atri[posicion] == '"color_fuente"':
                fuente = atri[1]
                print(fuente)
            elif atri[posicion] == '"forma"':
                forma = atri[1]
                print(forma)

        self.texto = 'digraph\treporte{'
        self.texto += '\n\t\trankdir="TB"'
        self.texto += f'\n\t\tlabel="{titulo}"'
        self.texto += f'\n\t\tlabelloc="t"'
        self.texto += f'\n\t\tnode[shape={forma} fontcolor={fuente} style="filled" fillcolor={fondo}]'
        self.texto += f'\n\t\tgraph[ordering="out"]'

        for op in self.operaciones:
            actual = op.evaluar()[posicion]
            self.texto += actual

        self.texto += '\n\n}'

        with open('Grafica.dot', 'w', encoding='utf-8') as archivo:
            archivo.write(self.texto)