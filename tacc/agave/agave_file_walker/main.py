from agavepy.agave import Agave
import sys

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print 'Usage <api_server> <token> <base_folder>'
    args = sys.argv[1:]
    url = args[0]
    token = args[1]
    base_folder = args[2]
    c = Agave(api_server = url, token = token)

