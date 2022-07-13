#!/user/bin/env python3
import urllib.request
import json
import webbrowser

# Define API
apiurl = 'https://api.nasa.gov/planetary/apod?'
demokey = 'api_key=DEMO_KEY' # using demo key in place of my key

# Calling webservice
apiurlobj = urllib.request.urlopen(apiurl + demokey)

# Reading the object
apiread = apiurlobj.read()

# decode json to python data structure
decodeapi = json.loads(apiread.decode('utf-8'))

# Display data

print("\n\nConverted python data")
print(decodeapi)

# use browser to open the URL

input('\nPress Enter to open NASA Picture of the Day in Firefox' )
webbrowser.open(decodeapi['url'])

