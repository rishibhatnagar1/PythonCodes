epsilon = 0.01 # Accuracy, how close you want your answer to be
#y = raw_input("Enter the number you want the square root of: ")
y = 90
guess = y/2.0

while abs(guess*guess - y) >= epsilon:
	guess = guess - (((guess**2.0)-y)/(2.0*guess))
	print ('Square root' + str(y) + 'is about' + str (guess))
