def hosts_get(zapi, group):
    # Get a list of hosts on a HostGroup
    hostgroup = zapi.hostgroup.get(
        output="extend",
        excludeSearch=True,
        filter={'name':group},
        selectHosts=['name']
    )

    count_hosts = 0
    for hg in hostgroup:
        print('Grupo: ' + hg['name'])

        for host in hg['hosts']:
            print('    Host: ' + host['name'])
            count_hosts += 1
        print(f'    Número de hosts: {count_hosts}')
        print('-=============-')
