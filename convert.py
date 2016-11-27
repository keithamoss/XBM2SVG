import os
from wand.image import Image

xbm_path = os.path.join(os.getcwd(), "xbm")

for infile in os.listdir(xbm_path):
    infile_path = os.path.join(xbm_path, infile)
    if os.path.isfile(infile_path):
        print infile

        with Image(filename=infile_path) as img:
            img.format = 'svg'
            img.save(filename='out/{}'.format(infile.replace('xbm', 'svg')))