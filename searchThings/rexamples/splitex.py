'''re.split uses pattern as amn argument which specifies the delimiter, we can use any text that matches the pattern as a delimiter to separate the text, it is available directly on a string and no regular expression is handeled, it is simpler'''
import re
count = 0
count_vow = 0
# Input string.
value = "one upon a T1me, 3ere was a crocodile, who 8 everything, 1 two 2 three 3"

# Separate on one or more non-digit characters.
result = re.split("\D+", value) #D is for non digit , + for one or more non digit
bla = re.split("\W+",value)
vow = re.split("[aeiou]",value)
# Print results.
for element in result:
    print(element)
for place in bla:
    count = count+ 1
for vowel in vow:
    count_vow = count_vow+1
	
print "spaces: ",count
print "vowels: ",count_vow
print vow
