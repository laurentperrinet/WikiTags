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

# generating a bunch of new names
## extarcting both sides
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
        print(bands_list[i_band])

#import os
