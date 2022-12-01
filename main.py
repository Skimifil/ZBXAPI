# Referencia: https://github.com/lukecyca/pyzabbix
from pyzabbix import ZabbixAPI
import dotenv
import os
from menu_new import menu

# Chamada do arquivo '.env' com as variaveis
dotenv.load_dotenv(dotenv.find_dotenv())

ZABBIX_API_URL = os.getenv('zbx_api_url')
UNAME = os.getenv('uname')
PWORD = os.getenv('pword')
FIEXP = os.getenv('file_export')


# Faz a conexão com a API e chama o menu
def callapi(zabbix_api_url, uname, pword, file_exp):
    zapi = ZabbixAPI(zabbix_api_url)
    zapi.login(uname, pword)
    zapi.session.verify = False
    zapi.timeout = 10.1
    # You can also authenticate using an API token instead of user/pass with Zabbix >= 5.4
    # zapi.login(api_token='xxxxx')
    print("Connected to Zabbix API Version %s" % zapi.api_version())
    file_export = open(file_exp, 'a')
    print('-=============-')
    menu(zapi, file_export)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    callapi(ZABBIX_API_URL, UNAME, PWORD, FIEXP)
