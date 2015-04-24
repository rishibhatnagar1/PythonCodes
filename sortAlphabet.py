''' This code will sort the strings on the basis of the alphabetical order '''

#Give an input as a list
list =['Steam','Potluch','spider','snow','Flake','adam','Eve']

#Sorting list according to various styles
''' if you use sorted() , the list will be sorted alphabatically, but the Captial letter will get more preference'''
print ("Captial Gets more preference: "),sorted(list)
print ("Doesn't matter if it is capital, sorts independently: "),sorted(list,key = str.lower)
print ("sort list reverse order: "),sorted(list,reverse = True)
print ("True reverse order: "),sorted(list,key =str.lower,reverse = True)
