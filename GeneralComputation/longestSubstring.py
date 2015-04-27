'''We have to find the longest substring in the input where all the alphabets have been arranged in the alphabatical order.
This is how I think this should be done.
1.Check each letter, if the letter has a greater weight than the next one, you check for the next letter.
In python "a" is smaller than "b" and "ab" is smaller than "ba", using this idea we can check if "abd" is smaller or bigger than "d". It is smaller than "d" by the way. This is how we are going to check the letters.
2.You save this in an empty string and check its length. The length of the current string should be more than the previous string for this to work '''

s = raw_input("Enter the string you want to find out: ")
print "Total length of the string is: ", len(s)
curString = s[0] #store temp values in this
longest =s[0]
for i in range(0,len(s)):
	if s[i] >=curString[-1]: #Checking for the alphabatical order here
		curString +=s[i] #append to the string
		if len(curString)> len(longest):
			longest = curString
		else:
			curString = s[i]

print "Longest sub string in alphabatical order is: ",longest
	
	
