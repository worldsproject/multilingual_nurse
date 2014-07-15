#!/usr/bin/python
# -*- coding: utf-8 -*-

from hashlib import sha1
import hmac
import json
import requests
import time

if __name__ == "__main__":

	PUBLIC_KEY = "}EPLC$}mzl(6eu8VO=Csw1B$ErOlntx4tEu6P$^_Wz9}S0TNlmlxd=~VVl-ot8Ht"
	PRIVATE_KEY = ")s$1RJcSlaBOr~j7{Rda7SmObWt{5tdT$ncRLh{vMuwMd1plP}Ys]yDyus)vyEtJ"
	URL = 'http://api.sandbox.gengo.com/v2/'

	RESPONSE_TYPE = 'json'

	header = {"Accept": "application/json"}
	
	data = {
		"api_key": PUBLIC_KEY,
		"api_sig": PRIVATE_KEY,
		"ts": str(int(time.time()))
		}
		
	#use your private key to make an hmac
	
	data["api_sig"] = hmac.new(data["api_sig"].encode(), data["ts"].encode(), sha1).hexdigest()
	
	job1 = {
        'slug': 'job test 1',
        'body_src': 'one two three four',
        'lc_src': 'en',
        'lc_tgt': 'ja',
        'tier': 'standard',
        'auto_approve': 1,
        'custom_data': 'some custom data untouched by Gengo.',
    }
	job2 = {
        'slug': 'job test 2',
        'body_src': 'five six seven eight',
        'lc_src': 'en',
        'lc_tgt': 'ja',
        'tier': 'standard',
        'comment': 'This one has a comment',
    }

	jobs = {'job_1': job1, 'job_2': job2}
	data["data"] = json.dumps({'jobs': jobs}, separators=(',', ':'))

	post_job = requests.post(URL, data=data, headers=header)
	res_json = json.loads(post_job.text)
	if not res_json["opstat"] == "ok":
		msg = "API error occured.\nerror msg: {0}".format(
            res_json["err"]
        )
		raise AssertionError(msg)
	else:
		print(res_json)

