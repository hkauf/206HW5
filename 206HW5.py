import re

infile = open("206HW5Data.txt", "r")
count = 0
for lines in infile:
	y = re.findall('[0-9]+', lines)
	for item in y:
		count = count + int(item)
print (count)