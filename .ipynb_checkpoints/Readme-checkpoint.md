## Image classifier by CNN

# File constitution
    ・identify.py --- main program
    ・get_image_from_flickr.py --- get image from Flickr to use FlickrAPI
    ・gen_data.py --- generate numpy

*判別したい画像名を指定し，ディレクトリ作成
　5つまでに制限
　画像の要不要判断は人力で選別する必要あり
　
　CNNでトレーニングし判断できるようにする

　その後，FlaskdeWebアプリ化

