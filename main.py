from pathlib import Path
from yandex import YaUploader

if __name__ == '__main__': 
    file_name = "1.txt"
    path_to_file = Path(file_name).resolve()

    token = 'AQAAAABY0AurAADLW6-vtuzRskabtPbhm55BoFo'
    url = 'https://cloud-api.yandex.net'

    uploader = YaUploader(token, url)
    directory = uploader.file_list()
    upload = uploader.upload(directory, file_name, path_to_file)