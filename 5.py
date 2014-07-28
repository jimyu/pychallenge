# uses banner.p, and unpickles it. then uses sys to print out the banner correctly. don't use print, as it adds an extra space between characters
import sys, pickle

f = open('banner.p', 'r')
x = pickle.load(f)
print '\n'.join([''.join([char*num for (char, num) in lst]) for lst in x])
