
import requests
import json

class YaUploader:

    def __init__(self, token, url):
        self.token = token
        self.main_url = url
    
    def get_headers(self):

        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'}

    def _get_link_for_upload(self, directory, file_name):
        headers = self.get_headers()
        url = f'{self.main_url}/v1/disk/resources/upload'
        params = {'path': f'{directory}/{file_name}' }
        get_href  = requests.get(url, headers=headers, params=params)
        get_href_json = json.loads(get_href.text)
        if get_href_json.get('message'):
            print(get_href_json['message'])
            return 
        return get_href_json['href']


    def upload(self, directory, file_name, path_to_file):
        headers = self.get_headers()
        href = self._get_link_for_upload(directory, file_name)
        if href:
            upload = requests.put(href, data=open(path_to_file, 'rb'))
            if upload.status_code == 201:
                print('Status: success')

    def file_list(self):
        url = f'{self.main_url}/v1/disk/resources/files/'       
        headers = self.get_headers()
        get_files  = requests.get(url, headers=headers)             
        directory = 'Files from Feride'
        
        result = json.loads(get_files.text)
        for item in result['items']:
            if directory in item['path']:
                return directory

        
        new_directory_url = f'{self.main_url}/v1/disk/resources'
        params = {'path': directory}
        headers = self.get_headers()
        new_directory  = requests.put(new_directory_url, headers=headers, params=params) 
        result = json.loads(new_directory.text)
        return directory
