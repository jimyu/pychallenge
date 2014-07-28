import string

# make string of original alphabet and the new alphabet,
# with all characters shifted by 2
org = string.ascii_lowercase
new = org[2:] + org[:2]

# make translation table to decipher code
tab = string.maketrans(org, new)
trans = raw_input('Enter the string to be deciphered: ')
print(trans.translate(tab))
