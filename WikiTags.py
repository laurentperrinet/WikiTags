__author__ = "Laurent Perrinet"
__licence__ = 'MIT'

ROOT = 'https://github.com/laurentperrinet/WikiTags/wiki/'
SEED = 42
BANDS = ['Talking Heads',
         'Dépèche Mode',
         'Dead Kennedys',
         'Neil Young',
         'Bob Dylan',
         'Georges Brassens',
         'Banana Rama',
         'Bob Marley',
         'Peter Tosh',
         'The Clash',
         'Mulatu Astatke',
         'Joe Strummer',
         'Rolling Stones',
         'Stone Roses',
         ]
VERB = True
N_X, N_Y = 8, 15 # columns, rows
RESULT = './grid.jpg'

# generating a bunch of new names
## extracting both sides
bands_pre, bands_post = [], []
for band in BANDS:
    (s1, s2) = band.split(' ')
    bands_pre.append(s1)
    bands_post.append(s2)
if VERB: print(bands_pre, bands_post)

## shuffling them
import itertools
bands_list = list(itertools.product(bands_pre, bands_post))
import numpy as np
np.random.seed(SEED)
ind_bands = np.random.permutation(len(BANDS)**2)
if VERB:
    for i_band in ind_bands:
        s1, s2 = bands_list[i_band]
        print(s1 + s2)


if VERB:
    url = ROOT + s1 + s2
    print(url)

import os
import pyqrcode
# https://pythonhosted.org/PyQRCode/rendering.html
# pip3 install pyqrcode
# pip3 install pypng

for i_band in ind_bands:
    s1, s2 = bands_list[i_band]
    figname = os.path.join('/tmp', s1 + s2 + '.png')
    if not os.isfile(figname):
        print('Generating', figname)
        url = ROOT + s1 + s2
        code = pyqrcode.create(url)
        code.png(figname, scale=5)

# alternatives
# image_as_str = code.png_as_base64_str(scale=5)
# html_img = '<img src="data:image/png;base64,{}">'.format(image_as_str)
# print(code.text())
# >>> code = pyqrcode.create('Are you suggesting coconuts migrate?')
# >>> image_as_str = code.png_as_base64_str(scale=5)
# >>> html_img = '<img src="data:image/png;base64,{}">'.format(image_as_str)
