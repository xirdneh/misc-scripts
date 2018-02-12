"""Tool to correctly use ssh keys on agave systems"""
import json
import sys
import getpass
from agavepy.agave import Agave

def _check_json_file(args):
    """Checks if user has given a json file as input and reads it"""
    json_file = None
    if len(args) > 1 and args[1].endswith('.json'):
        json_file = args[1]
        with open(json_file, 'r') as _file:
            json_file = _file.read()
    elif len(args) > 1 and not args[1].endswith('.json'):
        print "File input must be .json"
        sys.exit(1)

    return json_file

def _read_ssh_keys(args):
    if len(args) < 4:
        print "Need private key file path and public key file path"
        sys.exit(1)

    ssh_private_path = args[2]
    ssh_public_path = args[3]
    ssh_private_file = None
    ssh_public_file = None
    with open(ssh_private_path, 'r') as _file:
        ssh_private_file = _file.read()

    with open(ssh_public_path, 'r') as _file:
        ssh_public_file = _file.read()

    ssh_private_file = ssh_private_file.strip()
    ssh_public_file = ssh_public_file.strip()
    return ssh_private_file, ssh_public_file

def _prompt_details():
    system_type = raw_input("System Type [storage/execution]: ")
    available = raw_input("Available [true/false]: ")
    default = raw_input("default [false/true]: ")
    description = raw_input("Description [ ]: ")
    global_default = raw_input("Global Defaut [false/true]: ")
    system_id = raw_input("System Id [ ]: ")
    system_name = raw_input("System Name [ ]: ")
    if not system_type:
        system_type = 'storage'

    return {'systemType': system_type,
            'available': available,
            'default': default,
            'description': description,
            'globalDefault': global_default,
            'systemId': system_id,
            'systemName': system_name}

def _set_sshkeys_auth(json_obj, private_key, public_key):
    json_obj['storage']['auth'] = {
        'type': 'SSHKEYS',
        'privateKey': private_key,
        'publicKey': public_key,
        'username': json_obj['storage']['auth']['username']
    }
    return json_obj

def main(args):
    """main func"""
    print "system_create <json file> <private key> <public key>"
    json_file = _check_json_file(args)
    if not json_file:
        json_obj = _prompt_details()
    else:
        json_obj = json.loads(json_file)

    ssh_private_file, ssh_public_file = _read_ssh_keys(args)
    json_obj = _set_sshkeys_auth(json_obj, ssh_private_file, ssh_public_file)
    api_server = raw_input('Agave API server? ')
    token = getpass.getpass('Agave Token? ')
    print '{} : {}'.format(api_server, token)
    print json.dumps(json_obj, indent=2)
    client = Agave(api_server=api_server, token=token)
    if json_obj.get('id'):
        res = client.systems.update(systemId=json_obj['id'], body=json_obj)
    else:
        res = client.systems.add(body=json_obj)
    print res
    res = client.files.list(systemId=json_obj['id'], filePath='')
    print res

if __name__ == '__main__':
    main(sys.argv)
