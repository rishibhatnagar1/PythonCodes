''' For bubble Sort from a array, we need two tings, array, something where the individual things can be copied inot temporary and third the final array. As it turns out, you can do a swipe just by doing a a,b=b,a , so hoping to use that here.'''

alist1 =[10,'bat',30,'ball',1,2,3,34634,0,10,10,10,10,10,5,3,2,4,5,6,7,8,9,0,5,3,2,3,123,12,3,123,123,12,3,123,1,23,123,123,121,122]

def bubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1): #here the val of passnum will be the total length, it will decrement from the end basically
		for i in range(0,passnum):
			if alist[i]>alist[i+1]:
				temp = alist[i]
				alist[i] =alist[i+1]
				alist[i+1] = temp
				
	print alist			
def shortBubbleSort(alist):
	exchanges = True
	passnum = len(alist)-1
        while passnum > 0 and exchanges:
		exchanges = False
       		for i in range(passnum):
           		if alist[i]>alist[i+1]:
               			exchanges = True
               			temp = alist[i]
               			alist[i] = alist[i+1]
               			alist[i+1] = temp
       		passnum = passnum-1
	print alist

shortBubbleSort(alist1)
bubbleSort(alist1)

	
	
