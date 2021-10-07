import json

class Config:
    def __init__(self, file_name):
        global config
        self.file_name = file_name
        config = json.load(open(file_name))

    def getUrl(self):
        return config['url']
