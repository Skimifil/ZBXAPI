# Referencia: https://github.com/lukecyca/pyzabbix
from pyzabbix import ZabbixAPI
import dotenv
import os
from functions.hosts_get import hosts_get
from functions.triggers_get import triggers_get
from functions.maintenances_get import maintenances_get

# Chamada do arquivo .env
dotenv.load_dotenv(dotenv.find_dotenv())

ZABBIX_API_URL = os.getenv('zbx_api_url')
UNAME = os.getenv('uname')
PWORD = os.getenv('pword')


def callapi(zabbix_api_url, uname, pword):
    zapi = ZabbixAPI(zabbix_api_url)
    zapi.login(uname, pword)
    zapi.session.verify = False
    zapi.timeout = 10.1
    # You can also authenticate using an API token instead of user/pass with Zabbix >= 5.4
    # zapi.login(api_token='xxxxx')
    print("Connected to Zabbix API Version %s" % zapi.api_version())
    print('-=============-')


    '''
    # Validação dos alertas ativos
    triggers_get(zapi)

    # Get dos hosts em um Grupo espeficico
    grupos = ['Databases','azure']
    for gr in grupos:
        hosts_get(zapi,gr)
    '''

    # Get das manutenções e seus hosts
    maintenances_get(zapi)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    callapi(ZABBIX_API_URL, UNAME, PWORD)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
