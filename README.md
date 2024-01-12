# GERADOR DE XML DO PROTHEUS

Recupera e cria o XML de uma nota fiscal emitida no Protheus baseado
no número da Chave e/ou outros parametros de busca.

### Porque ?

Alguma vez você precisou de arquivos XML das notas fiscais que você emite ? Entrar no sistema, acessar a rotina da Sefaz, copiar o XML (em texto) e depois salvar no arquivo
foi uma grande dor de cabeça. Agora não mais. Com este script você consegue gerar o arquivo XML com
apenas um comando, basta você ter a chave da nota fiscal e então passar a chave para a linha de comando e pronto, XML gerado.

#### Como utilizar

Por ser um projeto feito em Python você vai precisar ter o Python instalado na sua máquina, este projeto foi desenvolvido usando o Poetry, que é uma ferramenta para gerenciamento de dependências mas pode ser utilizado com virtualenv também ou executado em ambiente local.

Com o Poetry instalado basta executar o comando

```
poetry shell
```

Então com o ambiente ativado você deve fazer a instalação das dependencias, execute o comando

```
poetry install
```

Pronto, agora você só precisa ter uma chave de NFE em mãos (que exista no seu ERP Protheus) e então executar o comando comando achave apos o comando.

```
task run -k chave_de_acesso_aqui
```

Onde -k indica que uma chave de acesso será repassada por paramêtro. Você também pode enviar uma planilha com chaves de acesso caso tenha uma. Abaixo a lista de opções disponiveis.

```
options:
  -h, --help            Exibe o menu de ajuda e sai
  -f ARQUIVO EXCEL, --file ARQUIVO EXCEL Gera todos os XML das chaves inclusas na coluna [Chave de Acesso]
  -c COLUNA, --column COLUNA  Nome da coluna que será usada para procurar as chaves
  -k CHAVE_ACESSO, --key CHAVE_ACESSO A chave de acesso para gerar o arquivo xml
```

### Agradecimentos

Este projeto é gratuito e com codigo livre, nunca será cobrado. Agradeço as pessoas abaixo pelo feedback e melhorias.

@plimo263 - Marcos Felipe da Silva Jardim
