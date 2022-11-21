import time, sys
from functions.hosts_get import hosts_get
from functions.triggers_get import triggers_get
from functions.maintenances_get import maintenances_get


def menu(zapi, file_export):
    print('Escolha a função que quer executar:')
    print('[0] - Sair')
    print('[1] - Alertas ativos')
    print('[2] - Manutenções')
    print('[3] - Hosts em um grupo')
    print('-=============-')

    escolha = int(input('Escolha a opção: '))
    while escolha < 0 or escolha > 3:
        print('Opção inválida, favor escolher uma opção correspondente ao menu.')
        escolha = int(input('Escolha a opção: '))
    else:
        if escolha == 0:
            print('Fechando...')
            for i in range(0, 5):
                sys.stdout.write("\r{}".format(i))
                sys.stdout.flush()
                time.sleep(1)
            exit()
        elif escolha == 1:
            triggers_get(zapi)
        elif escolha == 2:
            maintenances_get(zapi)
        elif escolha == 3:
            # grupos = ['ACFIN', 'AMAZONAS', 'ATENTO', 'CNU', 'CSE', 'FRG', 'FURB', 'GLP', 'JSL', 'LEADER', 'MARABRAZ', 'METRORIO', 'ODONTOPREV', 'OVD', 'PETZ', 'RIHAPPY', 'SASCAR', 'SERVICE', 'SODIMAC', 'TECH4', 'TERRALINGUA', 'UNIMED']
            grupos = ['azure', 'WebSites']
            for gr in grupos:
                hosts_get(zapi, gr, file_export)
            file_export.close()
            print('Arquivo de saida gerado!')
