#!/usr/bin/python
# -*- coding: utf-8 -*-

from hashlib import sha1
import hmac
import json
import requests
import time

def create_job(text, lang, tier='standard'):
	return {'slug': 'English to ' + lang, 'body_src':text, 'lc_src':'en', 'lc_tgt':lang, 'tier':tier, 'auto_approve':1}

if __name__ == "__main__":

	PUBLIC_KEY = "}EPLC$}mzl(6eu8VO=Csw1B$ErOlntx4tEu6P$^_Wz9}S0TNlmlxd=~VVl-ot8Ht"
	PRIVATE_KEY = ")s$1RJcSlaBOr~j7{Rda7SmObWt{5tdT$ncRLh{vMuwMd1plP}Ys]yDyus)vyEtJ"
	URL = 'http://api.sandbox.gengo.com/v2/translate/jobs'

	RESPONSE_TYPE = 'json'

	header = {"Accept": "application/json"}
	
	data = {
		"api_key": PUBLIC_KEY,
		"api_sig": PRIVATE_KEY,
		"ts": str(int(time.time()))
		}
		
	#use your private key to make an hmac
	
	data["api_sig"] = hmac.new(data["api_sig"].encode(), data["ts"].encode(), sha1).hexdigest()
	
	languages = {'de', 'es', 'fr', 'ar', 'zh', 'vi'}
	text = 'Point to how you are feeling. I am hungry. I am thirsty. I am tired. I am in pain. I am not feeling well. I need to go to the bathroom.'
	
	job_count = 1
	
	jobs = {}
	for lang in languages:
		jobs['job_' + str(job_count)] = create_job(text, lang)
		job_count = job_count +1

	
	data["data"] = json.dumps({'jobs': jobs}, separators=(',', ':'))

	post_job = requests.post(URL, data=data, headers=header)
	print(post_job.text)
	res_json = json.loads(post_job.text)
	if not res_json["opstat"] == "ok":
		msg = "API error occured.\nerror msg: {0}".format(
            res_json["err"]
        )
		raise AssertionError(msg)
	else:
		print(res_json)

