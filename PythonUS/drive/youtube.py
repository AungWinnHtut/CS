from typing import List, Tuple
import pandas as pd
from Google import Create_Service
from icecream import ic

def getChannelPlaylists(channelId: str):
    """returning only id will cost zero quota"""
    try:
        items = []
        response = service.playlists().list(
            channelId=channelId,
            maxResults=50,
            part='id'
        ).execute()
        items.extend(response.get('items'))
        nextPageToken = response.get('nextPageToken')

        while nextPageToken:
            response = service.playlists().list(
                channelId=channelId,
                maxResults=50,
                part='id',
                pageToken=nextPageToken
            ).execute()
            items.extend(response.get('items'))
            nextPageToken = response.get('nextPageToken')
        return items
    except Exception as e:
        print(e)
        return
    
def getMyChannelPlaylists():
    try:
        items = []
        response = service.playlists().list(
            mine=True,
            maxResults=50,
            part='id'
        ).execute()
        items.extend(response.get('items'))
        nextPageToken = response.get('nextPageToken')

        while nextPageToken:
            response = service.playlists().list(
                mine=True,
                maxResults=50,
                part='id',
                pageToken=nextPageToken
            ).execute()
            items.extend(response.get('items'))
            nextPageToken = response.get('nextPageToken')
        return items
    except Exception as e:
        print(e)
        return

def getPlaylistVideos(serviceInstance, playlistId: str) -> Tuple[List, str]:
    try:
        playlistItems = serviceInstance.playlists().list(
            part='snippet',
            id=playlistId
        ).execute()
        playlistTitle = playlistItems.get('items')[0]['snippet'].get('localized').get('title')

        maxResults = 50
        items = []

        response = serviceInstance.playlistItems().list(
            part='contentDetails,snippet',
            playlistId=playlistId,
            maxResults=maxResults
        ).execute()
        items.extend(response.get('items'))
        nextPageToken = response.get('nextPageToken')

        while nextPageToken:
            response = serviceInstance.playlistItems().list(
                part='contentDetails,snippet',
                playlistId=playlistId,
                maxResults=maxResults,
                pageToken=nextPageToken
            ).execute()
            items.extend(response.get('items'))
            nextPageToken = response.get('nextPageToken')
        return (items, playlistTitle)
    except Exception as e:
        print(e)
        return

def exportPlaylistToExcel(playlistItems: List, excelPath: str) -> None:
    try:
        if not excelPath.endswith('.xlsx'):
            print('Excel file path is invalid.')
            return     
        pd.xlwriter = pd.ExcelWriter(excelPath)
        df = pd.DataFrame(playlistItems)
        # for time saving, I am going to export everything
        df['snippet'].apply(pd.Series).to_excel(pd.xlwriter, sheet_name='snippet', index=False)
        df['contentDetails'].apply(pd.Series).to_excel(pd.xlwriter, sheet_name='contentDetails', index=False)
        pd.xlwriter.close()
        print('Export is saved at "{0}"'.format(excelPath))
    except Exception as e:
        print(e)
        return

if __name__ == '__main__':
    CLIENT_FILE = 'client-secret.json'
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube']
    service = Create_Service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)
    
    playlistIds = ['PLkNqzR4g-0EiBg1ef3mVGPPZZ5cnkBxAS']
    i = 0
    for playlistId in playlistIds:
        i += 1
        print(i)
        playlistItems, playlistTitle  = getPlaylistVideos(service, playlistId)
        # if a playlsit has no video, then there is nothign to exprot
        ic(playlistTitle)
        if playlistItems :
            exportPlaylistToExcel(playlistItems, 'Playist backup ({0}).xlsx'.format(playlistTitle))