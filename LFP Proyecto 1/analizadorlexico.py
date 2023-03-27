from Instrucciones.aritmeticas import *
from Instrucciones.trigonometricas import *
from Instrucciones.Errores import *
from Abstract.lexema import *
from Abstract.numero import *


#Aqui se definen los tokens que se van a utilizar en el analizador lexico
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


lexemas = list(reserved.values())

#Aqui se definen los tokens que se van a utilizar en el analizador lexico
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
    

    lexema = ''
    puntero = 0
    
    while cadena:       #Mientras la cadena no sea nula
        char = cadena[puntero]     #El char va a ser igual a la cadena en la posicion del puntero
        puntero += 1
        
        if char == '\"':           
            lexema, cadena = armar_lexema(cadena[puntero:]) #Mandamos la cedena como tal para no cortar nada  
            if lexema and cadena:  
                n_columnas +=1
                
                l = Lexema(lexema, n_lineas, n_columnas) 
                
                lista_lexemas.append(l)    #Se arma la cadena lexema
                n_columnas += len(lexema) +1  
                puntero = 0        #Reiniciamos el puntero
        elif char.isdigit():        #Si es un digito
            token, cadena = armar_numero(cadena) #Mandamos la cadena 
            if token and cadena:
                n_columnas +=1
                
                n = Numero(token, n_lineas, n_columnas)
                
                lista_lexemas.append(n)
                n_columnas += len(str(n)) +1  #Aqui se le suma 1 por el espacio que se le agrega al final
                puntero = 0
                
        elif char == '[' or char == ']':        #Si el char es igual a un corchete que cierra o abre
            
            c = Lexema(char, n_lineas, n_columnas)
            
            lista_lexemas.append(c)
            cadena = cadena[1:]
            n_columnas +=1
            puntero = 0
        elif char == '\t':        #Ignorar salto de linea
            n_columnas +=4
            cadena = cadena[4:]       #Corta espacios
            puntero = 0              #Reiniciamos el puntero
        elif char == '\n':         #Ignorar salto de linea      
            cadena = cadena[1:]
            puntero = 0
            n_lineas += 1
            n_columnas = 1
        elif char == ':' or char == ',' or char == '.' or char == '}' or char == '{' or char == '\r' or char == ' ':  #Si es un espacio o un salto de linea
            n_columnas += 1
            cadena = cadena[1:]
            puntero = 0
        else: 
            lista_errores.append(Errores(char, n_lineas, n_columnas)) #Aqui se agregan los errores
            cadena = cadena[1:]
            puntero = 0
            n_columnas += 1

    return lista_lexemas

#Armar lexema
def armar_lexema(cadena):
    global n_lineas
    global n_columnas
    global lista_lexemas
    lexema = ''
    puntero = ''
    for char in cadena:    #Recorrido de la cadena 
        puntero += char
        if char == '\"':      
            return lexema, cadena[len(puntero):]
        else:
            lexema += char
    return None, None #Return


#Armar numero
def armar_numero(cadena):
    numero = ''
    puntero = ''
    is_decimal = False      #Numeros decimales
    for char in cadena:
        puntero += char
        if char == '.':
            is_decimal = True 
        if char == '"' or char == ' ' or char == '\n' or char == '\t' or char== ']' or char== "}]":   #Si es un espacio o un salto de linea
            if is_decimal:
                return float(numero), cadena[len(puntero)-1:] #Retorna el numero y la cadena y se le resta 1 por el espacio que se le agrega al final
            else:
                return int(numero), cadena[len(puntero)-1:] #Retorna el numero y la cadena
        else:
            numero += char
    return None, None

def operar():
    global lista_lexemas
    global instrucciones
    operacion = ''
    n1 = ''
    n2 = ''
    while lista_lexemas:                            #Mientras la lista de lexemas no sea nula
        lexema = lista_lexemas.pop(0)       
        if lexema.operar(None) == 'Operacion':  
            if lista_lexemas:       
                operacion = lista_lexemas.pop(0)
        elif lexema.operar(None) == 'Valor1': #Si el lexema es igual a valor1
            n1 = lista_lexemas.pop(0)  #Se le asigna el valor1
            if n1.operar(None) == '[':
                n1 = operar()
        elif lexema.operar(None) == 'Valor2':
            n2 = lista_lexemas.pop(0)
            if n2.operar(None) == '[':
                n2 = operar()
    #Aqui se crea la instancia de la clase Aritmeticas
        if operacion and n1 and n2:
            return Aritmeticas(n1, n2, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n2.getFila()}:{n2.getColumna()}') 
    #Aqui se crea la instancia de la clase Trigonometricas
        elif operacion and n1 and operacion.operar(None) == ('Seno' or 'Coseno' or 'Tangente'):
            return Trigonometricas(n1, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
    return None



def operando():
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

    
