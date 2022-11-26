from datetime import datetime


def audit_get(zapi):
    now = datetime.now()
    now_timestamp = datetime.timestamp(now)
    get_timestamp = now_timestamp - 86400

    audit = zapi.auditlog.get(
        output="extend",
        sortorder="DESC",
        filter={'resourcetype': 4},
        time_from=int(get_timestamp),
        limit=2
    )

    for log_au in audit:
        print("O usuario: " + log_au['username'] + ", pelo IP: " + log_au['ip'])
        # TODO = Eu sei que tem um jeito mais fácil de fazer isso, só não lembro
        if log_au['action'] == '0':
            print("Executou a ação de Add o host " + log_au['resourcename'])
        elif log_au['action'] == '1':
            print("Executou a ação de Update o host " + log_au['resourcename'])
        elif log_au['action'] == '2':
            print("Executou a ação de Delete o host " + log_au['resourcename'])
        elif log_au['action'] == '4':
            print("Executou a ação de Logout o host " + log_au['resourcename'])
        elif log_au['action'] == '7':
            print("Executou a ação de Execute o host " + log_au['resourcename'])
        elif log_au['action'] == '8':
            print("Executou a ação de Login o host " + log_au['resourcename'])
        elif log_au['action'] == '9':
            print("Executou a ação de Failed login o host " + log_au['resourcename'])
        elif log_au['action'] == '10':
            print("Executou a ação de History clear o host " + log_au['resourcename'])
        elif log_au['action'] == '11':
            print("Executou a ação de Config refresh o host " + log_au['resourcename'])
        print("Segue os detalhes: \n" + log_au['details'])
        print('-=============-')
