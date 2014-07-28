# automatically print the new page, finding 'nothing is' and using the number that follows in the new url.
# takes in an input for when necessary
# modified with regex and group to avoid getting errors
import sys, re, urllib2

def main():
	base = 'http://pythonchallenge.com/pc/def/linkedlist.php?nothing='
	new = base + sys.argv[1]
	count = 400
	while (count > 0):
		page = urllib2.urlopen(new).read()
		ind = re.search('nothing is ([0-9]+)', page)
		print page
		if not ind: break
		new = base + ind.group(1)
		count -= 1

if __name__ == "__main__":
	main()
