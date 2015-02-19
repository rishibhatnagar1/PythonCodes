'''Challenge is to count the number of bob occurances'''

s = raw_input("Please enter a string to be tested: ")
total = 0
'''The best way to do this is to cut the given string into a group of 3 letters, starting from letter 0,1,2 and continuing this till we find the group equal to bob '''
for i in range(1,len(s)-1):
	if s[i-1:i+2] == "bob":
		total+=1
	
print "Total bobs is: ", total

