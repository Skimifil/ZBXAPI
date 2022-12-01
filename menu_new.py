from menu import *
from time import sleep
from functions.hosts_get import hosts_get
from functions.triggers_get import triggers_get
from functions.maintenances_get import maintenances_get
from functions.audit_get import audit_get


def menu(zapi, file_export):
    while True:
        resposta = menu_interface(['Sair', 'Alertas ativos', 'Manutenções', 'Hosts em um grupo', 'Audit'])
        if resposta == 0:
            cabecalho('Saindo do istema...')
            break
        elif resposta == 1:
            triggers_get(zapi)
        elif resposta == 2:
            maintenances_get(zapi)
        elif resposta == 3:
            # grupos = ['ACFIN', 'AMAZONAS', 'ATENTO', 'CNU', 'CSE', 'FRG', 'FURB', 'GLP', 'JSL', 'LEADER', 'MARABRAZ', 'METRORIO', 'ODONTOPREV', 'OVD', 'PETZ', 'RIHAPPY', 'SASCAR', 'SERVICE', 'SODIMAC', 'TECH4', 'TERRALINGUA', 'UNIMED']
            grupos = ['azure', 'WebSites']
            for gr in grupos:
                hosts_get(zapi, gr, file_export)
            file_export.close()
            cabecalho('Arquivo de saida gerado!')
        elif resposta == 4:
            audit_get(zapi)
        else:
            print('\033[31mERRO: Digite uma opção válida!\033[m')
        sleep(2)
