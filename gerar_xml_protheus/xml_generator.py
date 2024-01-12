import os

from gerar_xml_protheus.xml import XML

dir_base = os.path.dirname(__file__)

class XMLGenerator:
    ''' Cria o arquivo xml e pode salvar na pasta'''
    
    def __init__(self, xml: XML, output_dir: str = 'xml_folders' ) -> None:
        self.__xml = xml
        self.__output_dir = output_dir
    
    def save(self) -> str:
        ''' Salva o xml na pasta indicada usando como nome do arquivo a xml_key informada'''

        path_file = os.path.join(dir_base, self.__output_dir)

        try:
            os.mkdir(path_file)
        except Exception:
            pass

        path_file = os.path.join(path_file, f'{self.__xml.name}.xml')

        content = self.__xml.generate()

        with open(path_file, 'w', encoding='utf-8') as arq:
            arq.write(content)

