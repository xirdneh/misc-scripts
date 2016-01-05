from agavepy.agave import Agave
import sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Usage agave_test.py <api_server> <token> <path1> [<path2> ...]'
    args = sys.argv[1:]
    token = args[0]
    url = args[1]
    paths = args[2:]
    c = Agave(api_server = url, token='')
    resources = c.resources
    for api in resources['apis']:
        if api['path'] not in paths:
            continue
        for sub_api in api['api_declaration']['apis']:
            print('\033[0:32mPath: {0}\033[0:0m'.format(sub_api['path']))
            if len(sub_api['operations']) > 0:
                print('\033[0:31mOperations:\033[0:0m')
                for op in sub_api['operations']:
                    print('\t\033[0:35mNickname: {0}\033[0:0m'.format(op['nickname']))
                    print('\t\tMethod: {0}'.format(op['method']))
                    print('\t\tSummary: {0}'.format(op['summary']))
                    if len(op['parameters']) > 0:
                        print('\t\t\033[0:31mParameters:\033[0:0m')
                        for p in op['parameters']:
                            print('\t\t\t\033[0:33mName: {0}\033[0:0m'.format(p['name']))
                            print('\t\t\tType: {0}'.format(p['type']))
#                    i = input('\nPress any key to go to the next operation...') 
