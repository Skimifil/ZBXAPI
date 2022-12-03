from datetime import datetime
import requests


def audit_get(zapi):
    global message, subject_mess
    token = "TOKEN do ROBOT"
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

    def chama_tel_subject(token_robot, id_do_chat, subject_message):
        url_sub = f"https://api.telegram.org/bot{token_robot}/sendMessage?chat_id={id_do_chat}&text={subject_message}"
        print(requests.get(url_sub).json())

    def chama_tel_message(token_robot, id_do_chat, body_message):
        url = f"https://api.telegram.org/bot{token_robot}/sendMessage?chat_id={id_do_chat}&text={body_message}"
        print(requests.get(url).json())

    def printa_nome(username):
        user_name_too_string = str(username)
        print("O usuario: " + user_name_too_string + ", pelo IP: " + log_au['ip'])
        subjectmess = "O usuario: " + user_name_too_string + ", pelo IP: " + log_au['ip']

        chama_tel_subject(token, chat_id, subjectmess)

    for log_au in audit:
        if log_au['action'] == '0':
            user_name = log_au.get('username')
            printa_nome(user_name)

            print("Executou a ação de Add o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Add o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '1':
            user_name = log_au.get('username')
            printa_nome(user_name)

            print("Executou a ação de Update o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Update o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '2':
            user_name = log_au.get('username')
            printa_nome(user_name)

            print("Executou a ação de Delete o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Delete o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '4':
            user_name = log_au.get('username')
            printa_nome(user_name)

            print("Executou a ação de Logout o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Logout o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '7':
            user_name = log_au.get('username')
            printa_nome(user_name)

            print("Executou a ação de Execute o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Execute o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '8':
            user_name = log_au.get('username')
            printa_nome(user_name)

            print("Executou a ação de Login o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Login o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '9':
            user_name = log_au.get('username')
            printa_nome(user_name)

            print("Executou a ação de Failed login o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Failed login o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '10':
            user_name = log_au.get('username')
            printa_nome(user_name)

            print("Executou a ação de History clear o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de History clear o host " + log_au['resourcename'] + "\n" + "-=============-"

        elif log_au['action'] == '11':
            user_name = log_au.get('username')
            printa_nome(user_name)

            print("Executou a ação de Config refresh o host " + log_au['resourcename'] + "\n" + "-=============-")
            message = "Executou a ação de Config refresh o host " + log_au['resourcename'] + "\n" + "-=============-"

        chama_tel_message(token, chat_id, message)

        # print("Segue os detalhes: \n" + log_au['details'])
        # print('-=============-')
