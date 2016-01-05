#!/usr/bin/env python2.7
import urllib2
import urllib
import json
import base64
import pdb
import getpass
import requests
from requests.auth import HTTPBasicAuth

ARAPORT = 'https://agave.designsafe-ci.org'
#ARAPORT = 'https://api.araport.org'
#ARAPORT = 'https://api.tacc.utexas.edu'
ADAMA = ARAPORT + '/community/v0.3'
APPNAME = 'jcoronel_cli_dockerosx'

def get_keys(username, password):
    #response = requests.get(ARAPORT + '/clients/v2', auth=HTTPBasicAuth(username, password))
    pmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    pmgr.add_password(None, ARAPORT, username, password)
    h = urllib2.HTTPBasicAuthHandler(pmgr)
    opener = urllib2.build_opener(h)
    data = {"clientName": APPNAME}
    data = urllib.urlencode(data)
    response = opener.open(ARAPORT + '/clients/v2', data)
    json_data = json.loads(response.read())
    #json_data = response.json()
    return json_data

def get_auth_token(ck, cs, username, password):
    '''
        We don't use a password manager for the token since /token doesn't do "standard" authorization.
        This means that when urllib2 first tries to access the url it doesn't return a 401, this makes
        urllib2 to assume it doesn't need authentication and doesn't send the Auth header. We need
        to do this by hand.
    '''
    data = {'grant_type' : 'password',
            'username' : username,
            'password' : password,
            'scope' : 'PRODUCTION'
    }
    data = urllib.urlencode(data)
    up = base64.encodestring("{0}:{1}".format(ck, cs)).replace('\n', '')
    request = urllib2.Request(ARAPORT + "/token", data)
    request.add_header("Authorization", "Basic {0}".format(up))
    response = urllib2.urlopen(request)
    json_data = json.loads(response.read())
    return json_data

def call_uri(token, uri, method, data = None):
    print("Access endpoint: {0} \nHTTP Method: {1} \nData: {2}".format(ARAPORT + uri, method, data))
    if method == 'POST' or method == 'PUT':
        d = {}
        print('Data gotten: {0}'.format(data))
        #pdb.set_trace()
        for pair in data.split(','):
            key = pair.split(':')[0]
            value = pair.split(':')[1]
            d[key] = value
        data = urllib.urlencode(d)
        print('Data to send: {0}'.format(data))
    request = urllib2.Request(ARAPORT + uri, data)
    request.add_header("Authorization", "Bearer " + token)
    request.get_method = lambda: method
    try:
        response = urllib2.urlopen(request)
        json_data = json.loads(response.read())
        return True, json_data
    except urllib2.URLError as e:
        print("URLLIB2 Error: {0}".format(e.reason))
    
    return False, None

def start():
    username = raw_input("Username: ")
    password = getpass.getpass()
    keys_json_data = get_keys(username, password)
    print("Keys JSON: {0}".format(keys_json_data))
    consumerSecret = keys_json_data['result']['consumerSecret']
    consumerKey = keys_json_data['result']['consumerKey']
    print("Consumer Key: {0}".format(consumerKey))
    print("Consumer Secret: {0}".format(consumerSecret))
    token_json_data = get_auth_token(consumerKey, consumerSecret, username, password)
    print("Token JSON: {0}".format(token_json_data))
    token = token_json_data['access_token']
    print("Access Token: {0}".format(token))
    end = False
    while not end:
        option = raw_input("HTTP Method to use?\n")
        option = option.upper()
        uri = raw_input("URI to call\n")
        if option == 'GET' or option == 'PUT':
            success, data = call_uri(token, uri, option)
        elif option == 'POST' or option == 'PUT':
            data = raw_input("What's the data you want to send? (<key>:<value>[,<key>,<value>,...]\n")
            success, data = call_uri(token, uri, option, data)
        if success:
            print("Data back: {0}".format(json.dumps(data, sort_keys = True, indent = 4)))
            #for o in data["result"]:
            #    print("Building {0} #Floors = {1}".format(o["Building"], o["Number of  Floors"]));
        else:
            print("There was an error.")
        #option = raw_input("What do you want access?")

        option = raw_input("Again? \n 1 - Yes \n 2 - No\n")
        if option == "1":
            end = False
        else:
            end = True

if __name__ == '__main__':
    start()
