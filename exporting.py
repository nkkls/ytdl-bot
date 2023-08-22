import yt_dlp
import requests
import json
import os

class Exporter:
    def configure(self, filename, export_type, extension):
        if export_type == "audio":
            return {
                'format': 'm4a/bestaudio',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': extension,
                }],
                "outtmpl": f"./exports/{filename}",
            }
        else:
            return {
                'format': 'mp4/best',
                "outtmpl": f"./exports/{filename}.mp4",
            }
    
    def get_filesize(self, file):
        return (os.stat(file).st_size / 1024) / 1024
    
    def upload(self, file):
        files = {
            'reqtype': (None, 'fileupload'),
            'time': (None, '1h'),
            'fileToUpload': open(file, 'rb'),
        }

        response = requests.post('https://litterbox.catbox.moe/resources/internals/api.php', files=files)
        if response.status_code == 200:
            return response.content
        else:
            return -7
    
    def export(self, export_type, url, extension, upload = False):
        
        with yt_dlp.YoutubeDL() as ydl:
            try:
                info = ydl.extract_info(url, download=False)
                vti = info["title"]
                vil = info["duration"]
                vid = info['id']

                opts = self.configure(vid, export_type, extension)
            except:
                return -5
        
        with yt_dlp.YoutubeDL(opts) as ydl2:
            try:
                err = ydl2.download(url)
                if err:
                    return -2
            except:
                return -10
            
            file = f"./exports/{vid}.{extension}"
            if upload == True or self.get_filesize(file) > 20.0:
                file = self.upload(file)

            return [vid, vti, vil, file]
        
        

