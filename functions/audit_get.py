from datetime import datetime
import requests


def audit_get(zapi):
    global message, message_subject
    TOKEN = "TOKEN do ROBOT"
    chat_id = "ID do chat"

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
        # TODO = Ta uma merda esse código, mas estudo uma forma de refatorar depois
        if log_au['action'] == '0':
            user_name = log_au.get('username')
            user_name_to_string = str(user_name)
            print("O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip'])
            message_subject = "O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip']

            print("Executou a ação de Add o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Add o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '1':
            user_name = log_au.get('username')
            user_name_to_string = str(user_name)
            print("O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip'])
            message_subject = "O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip']

            print("Executou a ação de Update o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Update o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '2':
            user_name = log_au.get('username')
            user_name_to_string = str(user_name)
            print("O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip'])
            message_subject = "O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip']

            print("Executou a ação de Delete o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Delete o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '4':
            user_name = log_au.get('username')
            user_name_to_string = str(user_name)
            print("O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip'])
            message_subject = "O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip']

            print("Executou a ação de Logout o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Logout o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '7':
            user_name = log_au.get('username')
            user_name_to_string = str(user_name)
            print("O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip'])
            message_subject = "O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip']

            print("Executou a ação de Execute o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Execute o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '8':
            user_name = log_au.get('username')
            user_name_to_string = str(user_name)
            print("O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip'])
            message_subject = "O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip']

            print("Executou a ação de Login o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Login o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '9':
            user_name = log_au.get('username')
            user_name_to_string = str(user_name)
            print("O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip'])
            message_subject = "O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip']

            print("Executou a ação de Failed login o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Failed login o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '10':
            user_name = log_au.get('username')
            user_name_to_string = str(user_name)
            print("O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip'])
            message_subject = "O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip']

            print("Executou a ação de History clear o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de History clear o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '11':
            user_name = log_au.get('username')
            user_name_to_string = str(user_name)
            print("O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip'])
            message_subject = "O usuario: " + user_name_to_string + ", pelo IP: " + log_au['ip']

            print("Executou a ação de Config refresh o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Config refresh o host " + log_au['resourcename'] + "\n" + "-=============-"

        url_sub = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message_subject}"
        print(requests.get(url_sub).json())

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json())

        # print("Segue os detalhes: \n" + log_au['details'])
        # print('-=============-')
