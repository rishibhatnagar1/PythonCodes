s = raw_input("Please enter a string to be tested")
total = 0
for c in s:
	if c =='a' or c=='A' or c=='e' or c=='E' or c =='i' or c =='I' or c =='o' or c =='O' or c =='u' or c =='U':
		total +=1
print "Total number of vowels in the string is: ", total

