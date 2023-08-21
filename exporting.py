import yt_dlp
import requests

class Exporter:
    def __init__(self):
        self = self
    
    def upload(self):
        files = {
            'reqtype': (None, 'fileupload'),
            'time': (None, '1h'),
            'fileToUpload': open('meow.txt', 'rb'),
        }

        response = requests.post('https://litterbox.catbox.moe/resources/internals/api.php', files=files)
        print(response)
        return response