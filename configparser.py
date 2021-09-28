import json

def setConfig(FileName):
    global config
    config = json.load(open(FileName))

def getUrl():
    return config['url']
