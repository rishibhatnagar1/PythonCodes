'''For 1 to 100, multiples of 3 print fizz, multiple of 5 print buzz, multiple of both 3 and 5 print fizzbuzz '''

for i in range(1,101):
	if(i > 5) and (i % 3 == 0) and (i % 5 == 0):
		print "FizzBuzz"
	elif (i % 5 ==0):
		print "Buzz"
	elif (i % 3 == 0):
		print "Fizz"
	else:
		print str(i) 

