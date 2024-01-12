from dataclasses import dataclass
from datetime import date
from typing import Dict, List
import pymssql
from gerar_xml_protheus.xml import XML
from gerar_xml_protheus.xml_db_filter import XMLDBFilter


@dataclass
class XMLQuery:
    ''' Recupera os valores necessários para montar o xml'''

    user_db: str
    user_passwd: str
    db: str
    server: str
    port: int

    def __get_connect(self):
        ''' Retorna o conector do banco de dados '''
        con = pymssql.connect(
                user=self.user_db,
                password=self.user_passwd,
                database=self.db,
                host=self.server,
                port=self.port,
            )
        
        return con

    def __get_protocol(self, chv_list: List[str]) -> Dict[str, str]:
        ''' Realiza a consulta na SPED054 e traz o protocolo da nota'''
        SQL = f"""SELECT NFE_CHV, CONVERT(VARCHAR(MAX), 
        CONVERT(varbinary(max), XML_PROT)) AS XML FROM SPED054 WITH (NOLOCK) 
        WHERE NFE_CHV IN({','.join([f"'{i}'" for i in chv_list])})"""

        con = self.__get_connect()
        cur = con.cursor()
        cur.execute(SQL)

        prot_dicts = {reg[0]: reg[1].replace('\00', '') for reg in cur.fetchall() }

        con.commit()
        cur.close()
        con.close()

        return prot_dicts

    def __get_body_xml(self, chv_list: List[str]) -> Dict[str, str]:
        ''' Realiza a consulta na SPED050 e traz o corpo do xml'''
        SQL = f"""SELECT DOC_CHV, CONVERT(VARCHAR(MAX), 
        CONVERT(varbinary(max), XML_SIG)) AS XML FROM SPED050 WITH (NOLOCK) 
        WHERE DOC_CHV IN({','.join([f"'{i}'" for i in chv_list])})"""

        con = self.__get_connect()
        cur = con.cursor()
        cur.execute(SQL)

        body_dicts = {reg[0]: reg[1].replace('\00', '') for reg in cur.fetchall() }

        con.commit()
        cur.close()
        con.close()

        return body_dicts

    def get_xml(self, xml_key: str) -> XML:
        ''' Realiza a consulta no banco e retorna o xml que representa '''
        try:
            prot = self.__get_protocol([xml_key])[xml_key]
            body = self.__get_body_xml([xml_key])[xml_key]
        except KeyError as e:
            print(f"Chave ==> {xml_key} não encontrada no sistema.")
            exit(127)

        xml_itme = XML(xml_key, f"{body}{prot}")

        return xml_itme
    
    def get_xml_list(self, xmls: List[str]) -> List[XML]:
        ''' Recebe uma lista de chaves de acesso e gera os XML list pra todas '''
        prot = self.__get_protocol(xmls)
        body = self.__get_body_xml(xmls)

        xml_return = [ XML(xml_key, f"{body[xml_key]}{prot[xml_key]}") for xml_key in xmls if xml_key in prot and xml_key in body ]

        return xml_return

    def get_xml_by_date(self, date_from: date, date_to: date) -> List[XML]:
        ''' Realiza a consulta baseado na data de/ate e retorna todos os xmls envolvidos'''
        pass


    def get_xml_by_filter(self, filter_custom: XMLDBFilter) -> List[XML]:
        ''' Realiza uma consulta baseado no filtro customizado enviado'''
        pass