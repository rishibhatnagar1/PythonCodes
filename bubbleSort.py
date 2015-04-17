''' For bubble Sort from a array, we need two tings, array, something where the individual things can be copied inot temporary and third the final array. As it turns out, you can do a swipe just by doing a a,b=b,a , so hoping to use that here.'''

alist1 =[10,20,30,40,1,2,3,34634,0,10,10,10,10,10,5,3,2,4,5,6,7,8,9,0,5,3,2,3,123,12,3,123,123,12,3,123,1,23,123,123,121,122]

def bubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1): #here the val of passnum will be the total length, another loop to run from 0 to max val of length
		for i in range(0,passnum):
			if alist[i]>alist[i+1]:
				temp = alist[i]
				alist[i] =alist[i+1]
				alist[i+1] = temp
				#print alist[i],alist[i+1] 
	print alist			
bubbleSort(alist1)
#print(alist1)			
	
