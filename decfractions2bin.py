''' Take a number big enough to convert the fraction into a whole number, muliply the fraction with that power of 2, find the binary, then divide it by the same number again '''
x = float(raw_input("input value bewteen 0 and 1: "))

#We need to multiply this number with a power of 2 so that it becomes a whole number
p =0 # power of the number
while ((2**p)*(x) % 1) != 0: #remainder wrt 1 should be 0 for a whole number
	p +=1

num = int (x*(2*p))

''' This above section of the code will convert it to a figure that can be used to convert values to binary '''
result = ''
if num < 0:
	isNeg = True
	num = abs(num)

if num == 0:
	result == 0
while num > 2:
	result = result + str(num % 2)
	num = num / 2
for i in range (p - len(result)):
	result ='0' +result 
result = result [0:-p] +'.'+ result[-p:]
print ('binary respresentation of decimal' + str(x)+ 'is'+str(result))	
