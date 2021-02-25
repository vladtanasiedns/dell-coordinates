import os
import io
from quickstart import connect
from googleapiclient.http import MediaIoBaseDownload

file_ids = ['1weGptJr3CRBfrUpjcIjsUd8DqNb7vAaN']
file_names = ['Dell Data Velocity.csv']

drive_service = connect('drive', 'v3')

for file_id, file_name in zip(file_ids, file_names):
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False

    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

    fh.seek(0)

    with open(os.path.join('./', file_name), "wb") as f:
        f.write(fh.read())
        f.close()

# 116158511605-2fjqmr04pb1vfepqb7giutrauhkbmm7k.apps.googleusercontent.com
# XVG1rFIOwxBvXYWIxNM3RMFrx