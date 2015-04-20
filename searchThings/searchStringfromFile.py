import sys
import re

lines = open( sys.argv[1], "r" ).readlines()
count = 0
for line in lines:
	if re.search( r"heaven", line ):
		print line
		count +=1
print "Total count",count

