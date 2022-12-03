# Zabbix API e Dash

## Conceito

Com intuito de aprender Python, estou usando o meu trabalho com a ferramenta Zabbix para criar scripts de coleta de informação via API do Zabbix para trazer relatórios customizados.

Com isso irei utilizar outras tecnologias como banco de dados para armazenar informações, framework com o Dash para criação de Dashboards, exportação de dados para Excel e conceitos de *Data Science*.

## Execução

É preciso criar um arquivo ".env" na pasta raiz com a URL do Zabbix e as credenciais de acesso:

```shell
zbx_api_url = http://192.168.18.16/api_jsonrpc.php
uname = user
pword = pass
file_export = saida.txt
```

Coloquei o "file_export" para que ele faça uma saida em .txt para quando pede os Hosts por grupos.

## Atualizações

Próximos passos:
1. ~~Organizar um menu para seleção de qual função será usada~~
2. Criar um banco de dados em MongoDB para armazenar informações coletadas da API
3. Criar um export em Excel mais organizado
4. Criar mais funções (ainda não mapeado)
5. Criar um Dashboard utilizando o Framework Dash
6. Colocar TDD no código para testes