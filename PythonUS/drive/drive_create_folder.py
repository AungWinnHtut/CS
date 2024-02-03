from Google import Create_Service
CLIENT_SECRET_FILE = 'client-secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
file_metadata = {
    'name': '!TESTing', # if many folder? use list of folder names here
    'mimeType': 'application/vnd.google-apps.folder'
    # 'parents' : ['drive id']
}

service.files().create(body=file_metadata).execute()