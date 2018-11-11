import soundcloud
import SCcredentials

client = soundcloud.Client(
	client_id=SCcredentials.client_id,
	client_secret=SCcredentials.client_secret,
	username=SCcredentials.username,
	password=SCcredentials.password
)

def uploadtrack(trackname):
	print (trackname)
	track = client.post('/tracks', track={
		'title': trackname,
		'sharing': 'private',
		'asset_data': open(trackname, 'rb')
	})
	print (track.title)
