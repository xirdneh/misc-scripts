from agavepy.agave import Agave
import sys

import imp
afm = imp.load_source('AgaveFileManager', '/Users/xirdneh/projects/django/designsafe/portal/dsapi/agave/daos.py')
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def walk(c, system_id, folder, tab):
    files = c.files.list(systemId = system_id, filePath = folder)
    for f in files:
        if f['name'] == '.' or f['name'] == '..':
            continue
        af = afm.AgaveFolderFile(agave_client = c, file_obj = f)
        print '|' + '-' * tab + af.name
        print 'AgaveFile: {}'.format(af.as_json())
        m = af.save_as_metadata()
        if f['format'] == 'folder':
            walk(c, system_id, f['path'], tab + 1)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print 'Usage <api_server> <token> <systemId> <base_folder>'
    args = sys.argv[1:]
    url = args[0]
    token = args[1]
    system_id = args[2]
    base_folder = args[3]
    c = Agave(api_server = url, token = token)
    walk(c, system_id, base_folder, 0)   
