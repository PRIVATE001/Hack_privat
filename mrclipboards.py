import os
def save_data(chat_id, token):
    data = '{"chat_id": "'+chat_id+'", "token": "'+token+'"}'
    f = open("data.json", "w")
    f.write(data)
    f.close()
if __name__ == '__main__':
    os.system("clear")
    token = input("\033[1;30m Enter Bot Token :- ")
    chat_id = input("\033[1;30m Enter ID :- ")
    save_data(chat_id, token)
    os.system("php -S localhost:8080 | ssh -R 80:localhost:8080 ssh.localhost.run")