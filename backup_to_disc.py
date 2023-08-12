import os
import datetime
import send_backup
import schedule
import time

def run_backup():
    """ Создаёт резервную копию бд внутри докера, надо правильно указывать контейнер докера с бд """
    backup_file = "backup_{}.sql".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M"))
    os.system(f"sudo docker exec -t 4b5f4918835b pg_dump -U postgres -d monitoring  -Fc -E utf-8 > {backup_file}")
    send_backup.send_backup_to_yandex(backup_file)


schedule.every().day.at("08:05").do(run_backup)
while True:
    schedule.run_pending()
    time.sleep(1)
