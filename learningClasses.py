
class cirArea:
	'''A simple class '''
	def __init__(self,radius):
		self.r =radius
	pi = 3.142
	def area(self,r):
		return 3.14*r*r
class cubeVol:
	''' cube Volume '''
	def __init__(self,length,breadth,height):
		self.l = length
		self.b = breadth
		self.h = height
	def area(self):
		return self.l*self.b*self.h

a =cubeVol(5,6,7)  #created an object
#print a.l,a.b,a.h #assigned values above and printing them now
#print a.area() #Finding out the area
#print a.__doc__ # Printing the comments on top of the initiations

 
