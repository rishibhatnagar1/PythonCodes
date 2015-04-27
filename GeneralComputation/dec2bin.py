''' First step is to find out whether or not the number is neg. If it is negative, take an absolute value of the number otherwise not.
Initialize a string for result which stores the values in the end.
For bin , divide the number by 2, store the remained and concatenate that to a string. Remainder will be found using % , divide the number by 2 after that and keep moving '''

num = 1111191919191919191919

if num < 0:
	isNeg = True
	num = abs(num)
else:
	isNeg = False
result =''
if num == 0:
	result = '0'
while num >2 :
	result = str(num % 2) + result
	num = num/2
if isNeg:
	result = '-' +result

print "Value in bin is: ",result
