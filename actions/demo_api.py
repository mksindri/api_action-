#!/usr/bin/env python2

import sys
import requests as req

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, url):
	try:
		resp = req.get(url)
		print(resp.status_code)
		print(resp.url)
	except requests.exceptions.RequestExceptionas:
    		print ("Url cant be reached")
    		sys.exit(1)
	
