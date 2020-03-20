__author__ = "Laurent Perrinet"
__licence__ = 'MIT'

import subprocess
URL = subprocess.check_output(['git', 'remote',  'get-url', 'origin']).decode()
URL = URL.split('.git')[0] # stripping last bit given by github
ROOT = URL + '/wiki/'
print('ROOT =', ROOT)
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
VERB = True # verbose?
VERB = False # verbose?
N_X, N_Y = 5, 8 # columns, rows
N_X, N_Y = 8, 13 # columns, rows
N_X, N_Y = 5, 7 # columns, rows
RESULT = './grid.png' # name of the output file
MARGIN = 0.05 # margin around each axis
FONTSIZE = 14 # fontsize of the title of each axis
import numpy as np
PAPER_RATIO = np.sqrt(2)

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
    if not os.path.isfile(figname):
        print('Generating', figname)
        url = ROOT + s1 + s2
        code = pyqrcode.create(url)
        code.png(figname, scale=3)

# alternatives
# image_as_str = code.png_as_base64_str(scale=5)
# html_img = '<img src="data:image/png;base64,{}">'.format(image_as_str)
# print(code.text())
# >>> code = pyqrcode.create('Are you suggesting coconuts migrate?')
# >>> image_as_str = code.png_as_base64_str(scale=5)
# >>> html_img = '<img src="data:image/png;base64,{}">'.format(image_as_str)

import matplotlib.pyplot as plt

# Config:
dpi = 100 # dots per inches
figsize = 800/dpi # in inches

# Create plt plot:
fig, axs = plt.subplots(N_Y, N_X,
                        figsize=(N_X*figsize, N_Y*figsize))

for ii, i_band in enumerate(ind_bands[:(N_X*N_Y)]):
    s1, s2 = bands_list[i_band]
    figname = os.path.join('/tmp', s1 + s2 + '.png')
    url = ROOT + s1 + s2

    x_position = ii % N_X
    y_position = ii // N_X
    if VERB: print(ii, '/ (', x_position, ',', y_position, ') : ', figname)

    plt_image = plt.imread(figname)

    ax = axs[y_position, x_position]
    ax.imshow(plt_image, interpolation='nearest', cmap=plt.gray())
    ax.text(.5, 1-MARGIN, url, horizontalalignment='center',  fontsize=FONTSIZE, transform=ax.transAxes)
    # Hide grid lines
    ax.grid(False)

    # Hide axes ticks
    ax.set_xticks([])
    ax.set_yticks([])

plt.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0, hspace=MARGIN/2, wspace=MARGIN/2)
plt.savefig(RESULT, dpi=dpi)
