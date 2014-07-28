# uses the file 2.txt, which contains the "mess" from 'view-source:www.pythonchallenge.com/pc/def/ocr.html'
# requires you to unscramble the letters, as using a dictionary messes up the order

f = open('2.txt', 'r')
txt = f.read()

# use a dictionary to count the number of each character
dict = {}
# list that will hold the rare characters
rare = []

for char in txt:
	if char in dict:
		dict[char] += 1
	else:
		dict[char] = 1

for key in dict.keys():
	# assume rare means at most 5 occurrences
	if dict[key] <= 5:
		rare.append(key)

print rare
