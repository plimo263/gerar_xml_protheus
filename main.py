import sys 
import pandas as pd 
import argparse
from gerar_xml_protheus.xml import XML
from gerar_xml_protheus.xml_query import XMLQuery
from gerar_xml_protheus.xml_generator import XMLGenerator
from gerar_xml_protheus.extensions import (
    DB_MSSQL,
    USER_MSSQL,
    PASSWD_MSSQL,
    SERVER_MSSQL,
    PORT_MSSQL
)

msg = "Gera arquivos XML lendo dados da base do Protheus.Aceita chave digitada na linha ou um arquivo em Excel."

parser = argparse.ArgumentParser(
    description= msg
)

parser.add_argument('-f', '--file', dest='file', metavar='ARQUIVO EXCEL', nargs=1, help = 'Gera todos os XML das chaves inclusas na coluna [Chave de Acesso]')
parser.add_argument('-c', '--column', dest='column', metavar='COLUNA', default='Chave de Acesso', nargs=1, help = 'Nome da coluna que será usada para procurar as chaves')
parser.add_argument('-k', '--key', dest='key_nf', metavar='CHAVE_ACESSO', default='', nargs=1, help = 'A chave de acesso para gerar o arquivo xml')


def generate_from_excel(file: str, column: str):
    ''' Gera a lista de xml recebendo a planilha em excel'''
    with open(file, 'rb') as arq:
        pf = pd.read_excel(arq)
        result = pf[column]

        xml_list = [ chv_key for chv_key in result.values ]

        xml_query = XMLQuery(USER_MSSQL, PASSWD_MSSQL, DB_MSSQL, SERVER_MSSQL, PORT_MSSQL)

        xml_result = xml_query.get_xml_list(xml_list)

        for xml in xml_result:
            xml_printer = XMLGenerator(xml)
            xml_printer.save()

def generate_chv_nfe(chv_nfe: str):
    ''' Gera o arquivo xml recebendo uma uma chave de nota'''
    xml_query = XMLQuery(USER_MSSQL, PASSWD_MSSQL, DB_MSSQL, SERVER_MSSQL, PORT_MSSQL)

    xml_result = xml_query.get_xml(chv_nfe)

    xml_printer = XMLGenerator(xml_result)
    xml_printer.save()


if __name__ == '__main__':

    args = parser.parse_args()

    if args.file:
        filename = args.file[0] 
        column = 'Chave de Acesso' if not 'column' in args else args.column[0]
        generate_from_excel(filename, column)
    
    if args.key_nf:
        chv_nfe = args.key_nf[0]
        generate_chv_nfe(chv_nfe=chv_nfe)

