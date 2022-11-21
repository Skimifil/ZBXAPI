from datetime import datetime


def maintenances_get(zapi):
    maint = zapi.maintenance.get(
        output='extend',
        selectHosts='extend'
    )

    today = datetime.now()

    count_hosts = 0
    for mt in maint:
        print('Nome da manutenção: ' + mt['name'])

        # Get data inicio
        date_init_timestamp = int(mt['active_since'])
        date_init = datetime.fromtimestamp(date_init_timestamp)
        print('Manutenção iniciada: ' + str(date_init))

        # Get data fim
        date_fin_timestamp = int(mt['active_till'])
        date_fin = datetime.fromtimestamp(date_fin_timestamp)
        print('Manutenção será finalizada: ' + str(date_fin))

        # Get diferença
        difere_data_timestamp = date_fin_timestamp - int(today.timestamp())
        dias_para_fim = difere_data_timestamp / 86400
        dias_para_fim_round = round(dias_para_fim)
        if dias_para_fim_round > 0:
            print(f'Dias para finalizar: {dias_para_fim_round}')
        elif dias_para_fim_round == 0:
            print('Manutenção finalizada ou prestes a finalizar!')

        # Gera saída
        print('Host(s) dentro da manutenção:')
        for host in mt['hosts']:
            print('    ' + host['name'])
            count_hosts += 1
        print(f'    Número de hosts na manutenção: {count_hosts}')
        print('-=============-')