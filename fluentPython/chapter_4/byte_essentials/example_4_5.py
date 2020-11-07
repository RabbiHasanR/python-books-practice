# The string “El Niño” encoded with three codecs producing very different
# byte sequences.

for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')