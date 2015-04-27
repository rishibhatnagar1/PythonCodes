''' Class objects support two kind of operations, attribute reference and class instantiation '''

class cirArea:
	'''A simple class '''
	def __init__(self,radius): #This is a method for initialization of classes
		self.r =radius
	pi = 3.142
	def area(self,r):#this is a method
		return 3.14*r*r
class cubeVol:
	''' cube Volume '''
	def __init__(self,length,breadth,height):
		self.l = length
		self.b = breadth
		self.h = height
	def area(self): 
		return self.l*self.b*self.h

a =cubeVol(5,6,7)  #This is class instantiation, basically, initializing a class is what it is
#print a.l,a.b,a.h #assigned values above and printing them now
#print a.area() #Finding out the area , This is  attribute reference
#print a.__doc__ # Printing the comments in the class
''' This section is to prove that data attributes , can be made on the fly, all the calculation can be done without someone knowing what happened '''
a.circu = 9900
print a.circu


