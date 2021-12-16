#author:shapemind
#dt: 2021/12/16 17:40

from time import time
from threading import Thread
import requests

class DownloadHandler(Thread):
	
	def __init__(self, url):
		super().__init__()
		self._url = url
		
	def run(self):
		filename = self._url[self._ufl.rfind('/') + 1:]
		resp = requests.get(self._url)
		with open('/Users/Hao/' + filename, 'wb') as f:
			f.write(resp.content)

def main():
	resp = requests.get()