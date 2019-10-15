import csv
from tracks import *

header = ['playlist_id', 'track_name', 'track_uri', 'preview_url', 'added_at', 'analysis_url']
csv_data = [header]
for i in range(sleep_size):
    new_row = [sleep_id, tracks_name[i], tracks_uri[i], tracks_preview[i], tracks_addedAt[i], analysis_urls[i]]
    csv_data.append(new_row)

with open('tracks.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csv_data)
csvFile.close()
