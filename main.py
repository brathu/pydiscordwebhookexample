import requests
from configparser import Config
cg = Config('config/config.json')

notify_avatar = 'https://play-lh.googleusercontent.com/T_d7DoNH9W62dq8N-wYqTfr5vxDmya1_35kv_CpIO2ywZCnxqWDDg2iPbVcTXc1_qQ'


payload = {
	'avatar_url': notify_avatar,
	'username': 'example username',
	'content': 'example message'
}

req = requests.post(cg.getUrl(), data=payload)

