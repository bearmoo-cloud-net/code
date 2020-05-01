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
if options.port == '':
	rancherServer+= ":" + options.port
else:
	rancherServer+= ':8080'

#Here will connect to rancher Server using rancher API
rancherConnect = rancherAPI(rancherServer, options.accessKey, options.secretKey)

#Here will get all of the devices from zenoss master and remove all of the duplicates.
#rancherEnv = rancherConnect.getContainers()

rancherEnv = rancherConnect.getContainers()

count = 0
for res in rancherEnv['data']:
	if count == 0:
		x = PrettyTable()
		x.field_names = ["name", "HostID", "state", "Ip Address"]
		count+=1
	x.add_row([res['name'], res['hostId'], res['state'], res['primaryIpAddress']])

print (x)
