from __future__ import print_function

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

def list_folders(service):
    query = "mimeType = 'application/vnd.google-apps.folder'"

    results = service.files().list(
        q=query,
        fields="files(id, name)"
    ).execute()

    folders = results.get('files', [])

    if not folders:
        print('No folders found.')
    else:
        print('Folders:')
        for folder in folders:
            print(f"{folder['name']} (ID: {folder['id']})")

def list_files(service):
    files = service.files().list().execute().get('files', [])
    for f in files:
        print(f['name'], f['mimeType'])


SCOPES = 'https://www.googleapis.com/auth/drive.readonly.metadata'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('constants.json', SCOPES)
    creds = tools.run_flow(flow, store)
DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))


list_folders(DRIVE)
list_files(DRIVE)