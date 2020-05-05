from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

#Imformation of API key
key = "287ae990df38ef7f62319d159ac1b9a8"
secret = "261a31582256c41d"
wait_time = 1

#save directory
searchname1 = sys.argv[1]
searchname2 = sys.argv[2]
searchname3 = sys.argv[3]

#make new directory for image save
savedir = "./" + "images"





flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = searchname,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']
# check flickrapi json
# pprint(photos)

#get photo file 
for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'

    # check file exist or not
    if os.path.exists(filepath): continue
    # download photo file
    urlretrieve(url_q, filepath)
    # 1se sleep for server stress
    time.sleep(wait_time)


