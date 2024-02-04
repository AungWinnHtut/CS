from googleapiclient.http import MediaFileUpload
from Google import Create_Service
from googleapiclient.discovery import build
import os

CLIENT_SECRET_FILE = 'client-secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']


FOLDER_ID = '1sW0gTuHhW1yyF8d-S5RccI4adYLGqpCI'

def list_files_in_folder(service, folder_id):
    results = service.files().list(
        q=f"'{folder_id}' in parents",
        fields="files(id, name, mimeType)"
    ).execute()
    files = results.get('files', [])

    return files

def main():    
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    files = list_files_in_folder(service, FOLDER_ID)

    if not files:
        print('No files found.')
    else:
        file_list = [{'file_id': file['id'], 'file_name': file['name'], 'mime_type': file['mimeType']} for file in files]
        for file_info in file_list:
            print(file_info)

if __name__ == '__main__':
    main()