#!/usr/bin/env python

# Import libraries
import os
import json
import sys

from prettytable import PrettyTable
from inputoutput import cliOptions
from rancherapi  import rancherAPI
(options,args)   = cliOptions()
rancherServer    = ""

if options.accessKey == '':
	print ("A access key is needed.")
if options.secretKey == '':
	print ("A secret key is needed.")
if options.rancherHost == '':
	print ("A rancherHost is needed.")
else:
	rancherServer=options.rancherHost
#if options.port == '':
#	rancherServer+= ":" + options.port
#else:
#	rancherServer+= ':8080'

#Here will connect to rancher Server using rancher API
rancherConnect = rancherAPI(rancherServer, options.accessKey, options.secretKey)

#Here will get all of the devices from zenoss master and remove all of the duplicates.
#rancherEnv = rancherConnect.getContainers()

rancherEnv = rancherConnect.getHost()

count = 0
for res in rancherEnv['data']:
	if count == 0:
		x = PrettyTable()
		x.field_names = ["State", "Enviroment", "Hostname", "IP Address"]
		count+=1
	x.add_row([res['state'], res['accountId'], res['hostname'], rancherConnect.getHostIpAddress(res['id'])])

print (x)
