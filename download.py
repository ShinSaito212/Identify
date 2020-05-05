from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

#Imformation of API key
key = ""
secret = ""
wait_time = 1

###
savedir_root = "./" + "images"
image_name = []

for i in range(len(sys.argv) - 1):
 
    #make new directory for image save
    savedir_path = os.path.join(savedir_root, sys.argv[i + 1])
    os.mkdir(savedir_path)
    image_name.append(sys.argv[i + 1])


    #get flickr data as json
    flickr = FlickrAPI(key, secret, format='parsed-json')
    result = flickr.photos.search(
        text = image_name[i],
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
    for j, photo in enumerate(photos['photo']):
        url_q = photo['url_q']
        filepath = savedir_path + '/' + photo['id'] + '.jpg'

        # check file exist or not
        if os.path.exists(filepath): continue
        # download photo file
        urlretrieve(url_q, filepath)
        # 1se sleep for server stress
        time.sleep(wait_time)

