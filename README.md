# Zabbix API e Dash

Com intuito de aprender Python, estou usando o meu trabalho com a ferramenta Zabbix para criar scripts de coleta de informação via API do Zabbix para trazer relatórios customizados.

Com isso irei utilizar outras tecnologias como banco de dados para armazenar informações, framework com o Dash para criação de Dashboards, exportação de dados para Excel e conceitos de *Data Science*.

É preciso criar um arquivo ".env" na pasta raiz com as credenciais:
``bash
zbx_api_url = http://192.168.18.16/api_jsonrpc.php
uname = user
pword = pass
``