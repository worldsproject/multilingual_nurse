#!/usr/bin/python
# -*- coding: utf-8 -*-

from hashlib import sha1
import hmac
import json
import requests
import time

PUBLIC_KEY = "}EPLC$}mzl(6eu8VO=Csw1B$ErOlntx4tEu6P$^_Wz9}S0TNlmlxd=~VVl-ot8Ht"
PRIVATE_KEY = ")s$1RJcSlaBOr~j7{Rda7SmObWt{5tdT$ncRLh{vMuwMd1plP}Ys]yDyus)vyEtJ"
URL = 'http://api.sandbox.gengo.com/v2/translate/jobs/'

data = {
		"api_key": PUBLIC_KEY,
		"api_sig": PRIVATE_KEY,
		"ts": str(int(time.time())),
		}
		
#use your private key to make an hmac
	
data["api_sig"] = hmac.new(data["api_sig"].encode(), data["ts"].encode(), sha1).hexdigest()
data['data'] = {}

d = requests.post(URL + '269816', data=data)
print(d.text)
