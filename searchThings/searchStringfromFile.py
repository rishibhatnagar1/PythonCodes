import sys
import re

lines = open( sys.argv[1], "r" ).readlines()
count = 0
for line in lines:
	
	if re.search( r"Happy", line ) or re.search(r"sad",line) or re.search(r"unusual",line):
		print line
		count +=1
print "emotional count",count

