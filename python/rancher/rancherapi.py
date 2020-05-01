#!/bin/python
'''Python module to work with the rancher JSON API
'''
import ast
import re
import json
import logging
import requests

class rancherException(Exception):
    '''Custom exception for rancher
    '''
    pass

class rancherAPI(object):
  '''A class that represents a connection to a rancher server
  '''

  def __init__(self, host, accessKey, secretKey, ssl_verify=True):
    self.__host = host
    self.__session = requests.Session()
    self.__session.auth = (accessKey, secretKey)
    self.__session.headers = {'Content-Type': 'application/json'}
    self.__session.verify = ssl_verify
    self.__req_count = 0

  def requestSubmit(self, method, urlPath, data):
    if method == 'get':
      responds=self.__session.get(self.__host + urlPath)

    if method == 'post':
     responds=self.__session.post(self.__host + urlPath, data)

    return responds
  def getEnviroment(self):
    r = self.requestSubmit('get' ,'/v1/projects', data='')
    return r.json()

  def findEnviroment(enviroment):
    r = self.requestSubmit('get' ,'/v1/projects', data='')
    for i in r['id']:
        if i['name'] == enviroment:
	  return i['id']

  def getHost(self):
    r = self.requestSubmit('get' ,'/v1/hosts', data='')
    return r.json()

  def getHostIpAddress(self, hostId):
    r = self.requestSubmit('get' ,'/v1/hosts/' + hostId, data='').json()
    return r['data']['fields']['agentIpAddress']

  def getContainers(self):
    r = self.requestSubmit('get' ,'/v1/containers', data='')
    return r.json()

  def DeleteContainers(self):
    r = self.requestSubmit('DELETE' ,'/v2-beta/projects/1a5/containers/1i177369', data='')
    return r.json()

#//  def UpgradeContainer(self, containerName):
#//   r = self.requestSubmit('POST',)
#//"inServiceStrategy": {
#//  "launchConfig": {
#//    "tty":true,
#//    "vcpu":1,
#//    "imageUuid":"docker:ubuntu:14.04.3"
#//    //...and other parameters of  your existing service's launch config
#  }
#}


  def addGenericMachine(self, enviroment, ipaddress, description, Mconfig, hostName):
    Env = findEnviroment(enviroment)
    urlpath='/v1/projects/' + enviroment +'/machines'
    data = {"authKey":'', "labels": {"services": "yes"}, "engineInstallUrl": "https://get.docker.com", "engineStorageDriver": ''}
    data.update({"authCertificateAuthority": '', "name": hostName, "dockerVersion": '', "engineStorageDriver": '', "description": description})
    data.update({"genericConfig": { "ipAddress": ipaddress, "sshKey": "", "sshPort": "22", "sshUser": sshUser }})
    results=requests.post(hostname + ':' + port + urlpath, auth=(accessKey,secretKey), headers=headers, data=data)
    return data, urlpath

#  def stopContainer():
#    print ("Still in the works.")
    #'http://10.10.5.10:8080/v1/projects/1a5/containers/1i13561/?action=stop'
    #'http://10.10.5.10:8080/v1/projects/1a5/containers/1i13561/?action=purge'
