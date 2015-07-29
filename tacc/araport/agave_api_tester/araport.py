import urllib2
import urllib
import json
import base64
import pdb

ARAPORT = 'https://api.araport.org'
ADAMA = ARAPORT + '/community/v0.3'
USERNAME = 'jcoronel'
PASSWORD = 'nln1kwyrt'
APPNAME = 'my_cli_app'

def get_keys():
    pmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    pmgr.add_password(None, ARAPORT, USERNAME, PASSWORD)
    h = urllib2.HTTPBasicAuthHandler(pmgr)
    opener = urllib2.build_opener(h)
    data = {'clientName':APPNAME}
    data = urllib.urlencode(data)
    response = opener.open(ARAPORT + '/clients/v2', data)
    json_data = json.loads(response.read())
    return json_data

def get_auth_token(ck, cs):
    '''
        We don't use a password manager for the token since /token doesn't do "standard" authorization.
        This means that when urllib2 first tries to access the url it doesn't return a 401, this makes
        urllib2 to assume it doesn't need authentication and doesn't send the Auth header. We need
        to do this by hand.
    '''
    data = {'grant_type' : 'password',
            'username' : USERNAME,
            'password' : PASSWORD,
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
    if method == 'POST':
        d = {}
        print('Data gotten: {0}'.format(data))
        pdb.set_trace()
        for pair in data.split(','):
            key = pair.split(':')[0]
            value = pair.split(':')[1]
            d[key] = value
        data = urllib.urlencode(d)
        print('Data to send: {0}'.format(data))
        request = urllib2.Request(ARAPORT + uri, data)
    else:
        request = urllib2.Request(ARAPORT + uri)
    request.add_header("Authorization", "Bearer " + token)
    try:
        response = urllib2.urlopen(request)
        json_data = json.loads(response.read())
        return True, json_data
    except urllib2.URLError as e:
        print("URLLIB2 Error: {0}".format(e.reason))
    
    return False, None

def start():
    keys_json_data = get_keys()
    #print("Keys JSON: {0}".format(keys_json_data))
    consumerSecret = keys_json_data['result']['consumerSecret']
    consumerKey = keys_json_data['result']['consumerKey']
    print("Consumer Key: {0}".format(consumerKey))
    print("Consumer Secret: {0}".format(consumerSecret))
    token_json_data = get_auth_token(consumerKey, consumerSecret)
    #print("Token JSON: {0}".format(token_json_data))
    token = token_json_data['access_token']
    print("Access Token: {0}".format(token))
    end = False
    while not end:
        option = raw_input("1 - GET \n 2 - POST\n")
        uri = raw_input("URI to call\n")
        if option == "1":
            success, data = call_uri(token, uri, 'GET')
        elif option == "2":
            data = raw_input("What's the data you want to send? (<key>:<value>[,<key>,<value>,...]\n")
            success, data = call_uri(token, uri, 'POST', data)
        if success:
            print("Data back: {0}".format(json.dumps(data, sort_keys = True, indent = 4)))
        else:
            print("There was an error.")

        option = raw_input("Again? \n 1 - Yes \n 2 - No\n")
        if option == "1":
            end = False
        else:
            end = True

if __name__ == '__main__':
    start()
