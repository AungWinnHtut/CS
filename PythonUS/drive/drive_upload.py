from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'client-secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# Upload a file
file_metadata = {
    'name': 'Google.py',
    'parents': ['1oh1S-p3Zv7Ig19Q3FAk2OQbWfktj8-2J']
}

media_content = MediaFileUpload('Google.py', mimetype='text/plain')

file = service.files().create(
    body=file_metadata,

    media_body=media_content
).execute()

print(file)


# Replace Existing File on Google Drive
# file_id = '<file id>'

# media_content = MediaFileUpload('mp4.png', mimetype='image/png')

# service.files().update(
#     fileId=file_id,
#     media_body=media_content
# ).execute()