from Abstract.abstract import Expression


class Errores(Expression):
    
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)
        
    def operar(self, no):
        error_info = {
            "No.": no,
            "Descripcion-Token": {
                "Lexema": self.lexema,
                "Tipo": "Error Leximo",
                "Fila": self.fila,
                "Columna": self.columna
            }
        }
        
        return self._format_error_info(error_info)
    
    def _format_error_info(self, error_info):
        formatted_error_info = "{\n"
        for key, value in error_info.items():
            formatted_error_info += f'\t"{key}": '
            if isinstance(value, dict):
                formatted_error_info += "{\n"
                for sub_key, sub_value in value.items():
                    formatted_error_info += f'\t\t"{sub_key}": {sub_value}\n'
                formatted_error_info += "\t}\n"
            else:
                formatted_error_info += f'{value}\n'
        formatted_error_info += "}"
        return formatted_error_info
    
    def getColumna(self):
        return super().getColumna()
    
    def getFila(self):
        return super().getFila()