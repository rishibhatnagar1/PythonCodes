'''For , in checks for all the characters in a list, tuple or string '''
str1 ="I have a lazy dog"

for "dog" in str1:
	print "yup, present"
'''Identity operators compare memory lcations of objects, checks if two vals have same datatypes and values '''
a = 42
b ='42'

if a is b:
	print"true"
else:
	print "false"
# In the above case, both pointing to different objects, hence, you will get a false

if a is not b:
	print "true"
