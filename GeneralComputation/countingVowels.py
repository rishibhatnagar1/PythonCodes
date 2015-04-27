''' User will have to input a string to be tested and the code is going to find the number of vowels '''


s = raw_input("Please enter a string to be tested: ")
print "length of the string is: ",len(s)
total = 0
for c in s:
	if c =='a' or c=='A' or c=='e' or c=='E' or c =='i' or c =='I' or c =='o' or c =='O' or c =='u' or c =='U':
		total +=1
print "Total number of vowels in the string is: ", total

