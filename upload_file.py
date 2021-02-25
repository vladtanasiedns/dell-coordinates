import os
import io
from quickstart import connect
from googleapiclient.http import MediaFileUpload

drive_service = connect('drive', 'v3')


file_metadata = {'name': 'Dell Data Velocity.csv'}

media = MediaFileUpload('Dell Data Velocity.csv', mimetype='text/csv')

file = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()

print('File ID: %s' % file.get('id'))