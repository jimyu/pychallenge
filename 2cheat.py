# 'cheats' by finding all letters in the mess, rather than looking for rare characters
import string

f = open('2.txt', 'r')
txt = f.read()
alpha = string.ascii_lowercase
rares = []

for char in txt:
	if char in alpha:
		rares.append(char)

print rares
