from dataclasses import dataclass

@dataclass
class XML:

    name: str 
    content: str


    def __init(self) -> str:
        ''' Cria o cabecalho do xml'''
        return '<?xml version="1.0" encoding="UTF-8"?><nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00">'
    
    def __end(self) -> str:
        ''' Fecha o xml gerado'''
        return '</nfeProc>'
    
    def generate(self) -> str:
        ''' Gera o XML em String e a retorna'''
        return f"{self.__init()}{self.content}{self.__end()}"
