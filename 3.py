# uses '3.txt', which contains the characters in 'view-source:www.pythonchallenge.com/pc/def/equality.html'
import re

f = open('3.txt', 'r')
txt = f.read()

matches = re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', txt)
for match in matches:
	print match[4],
