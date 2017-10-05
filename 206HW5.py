import re
# def CountNumbers(file):
	
	# infile = open(file, "r")
infile = open("206HW5Data.txt", "r")
for lines in infile:
	y = re.findall('[0-9]+', infile)
print (y)



