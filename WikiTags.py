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
         'The Clash',
         'Mulatu Astatke',
         'Joe Strummer',
         'Rolling Stones',
         'Stone Roses',
         ]

# generating a bunch of new names
bands_pre, bands_post = [], []
for band in BANDS:
    (s1, s2) = band.split(' ')
    bands_pre.append(s1)
    bands_post.append(s2)
print(bands_pre, bands_post)
