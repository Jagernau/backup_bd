import yadisk
from dotenv import dotenv_values
env_dict = dotenv_values('.env')
DISK_TOKEN: str = str(env_dict["DISK_TOKEN"])


y = yadisk.YaDisk(token=DISK_TOKEN)

def send_backup_to_yandex(name_file: str):
    """ Отправляет резервную копию на яндекс диск """
    y.upload(f"{str(name_file)}", f"backup_bd/{str(name_file)}", timeout=500)
