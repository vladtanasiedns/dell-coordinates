import io
import os
from googleapiclient.http import MediaIoBaseDownload
from connect import connect

drive_service = connect()

file_ids = ['12-9C0CmNDU240vlnXzUjF4DD9DHlMlV0']
file_names = ['Dell Data Velocity.csv']

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