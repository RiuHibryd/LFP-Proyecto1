#Patron, Lexema, Token
#Diccionarios
reserved = {
    'ROPERACION' : 'Operacion',
    'RVALOR1'    : 'Valor1',
    'RVALOR2'    :  'Valor2',
    'RSUMA'      : 'Suma',
    'RRESTA'     : 'Resta',
    'RMULTIPLICACION':'Multiplicacion',
    'RDIVISION' : 'Division',
    'RPOTENCIA' : 'Potencia',
    'RRAIZ'     : 'Raiz',
    'RINVERSO'  : 'Inverso',
    'RSENO'     : 'Seno',
    'RCOSENO'   : 'Coseno',
    'RTANGENTE' : 'Tangente',
    'RMODULO'   : 'Modulo',
    'RTEXTO'    : 'Texto',
    'RCOLORFONDONDO' : 'Color-Fondo-Nodo',
    'RCOLORFUENTENODO' : 'Color-Fuente-Nodo',
    'RFORMANODO' : 'Forma-Nodo',
    'COMA'      : ',',
    'PUNTO'     : '.',
    'DPUNTOS'   : ':',
    'CORI'      : '[',
    'CORD'      : ']',
    'LLAVEI'    : '{',
    'LLAVED'    : '}',

}
lexemas = list(reserved.values())
global n_linea
global n_columna
global instrucciones
global lista_lexemas
n_linea = 1
n_columna = 1
#instrucciones
def instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = 0
    while cadena:
        char = cadena[puntero]
        puntero += 1
        if char == '\"':
            lexema, cadena = armar_lexema(cadena[puntero:])


def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = ''
    for char in cadena:
        puntero += char
        if char == '\"':
            return lexema, cadena[len(puntero):]
        else:
            lexema += char
           
    
