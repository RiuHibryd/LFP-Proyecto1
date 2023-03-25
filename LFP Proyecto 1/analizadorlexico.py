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
lista_lexemas = []
instrucciones = []
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
            if lexema and cadena:
                n_columna += 1
                #Armar Lexema
                lista_lexemas.append(lexema)
                n_columna += len(str(lexema)) + 1 
                puntero = 0
        elif char.isdigit():
            token, cadena = armar_numero(cadena)
            if token and cadena:
                n_columna += 1
                lista_lexemas.append(token)
                n_columna += len(str(token)) +1
                puntero = 0
            
               
        elif char == "\t":
            n_columna += 4
            cadena = cadena[4:]
            puntero =  0
        elif char == "\n":
            cadena = cadena[1:]
            puntero = 0
            n_linea += 1
            n_columna = 1
        else:
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
    for lexema in lista_lexemas:
        print(lexema)


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
           
    return None, None
def armar_numero(cadena):
    numero = ''
    puntero = ''
    is_decimal = False
    for char in cadena:
        puntero += char
        if char == '.':
            is_decimal = True
        if char == ' ' or char == '"' or char == '\n' or char == '\t':
            if is_decimal:
                return float(numero), cadena[len(puntero)-1:]
            else:
                return int(numero), cadena[len(puntero)-1:]
        else:
            numero += char