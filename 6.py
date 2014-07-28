# challenge 6, CHANNEL
# uses the files in folder channel.zip
# more nothings, re-using similar concept from challenge 4
import re, zipfile

zipfiles = zipfile.ZipFile('channel.zip')

first = '90052'
lst = [first]
ext = '.txt'
content = zipfiles.open(first + ext).read()
print content
new = re.search('nothing is ([0-9]+)', content)
while new:
	first = new.group(1)
	lst.append(first)
	content = zipfiles.open(first + ext).read()
	print content
	new = re.search('nothing is ([0-9]+)', content)

print ''.join([zipfiles.getinfo(name + ext).comment for name in lst])
