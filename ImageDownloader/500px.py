import urllib
link = raw_input("Enter the photo link: ")
name = raw_input("Enter a name for the photo: ")
f = urllib.urlopen(link)
''' Once the link is opened, the source of the link needs to be read '''
pageResource = f.read()
''' The code searches for this pattern '''
pattern="{\"size\":2048,\"url\":"
''' This will be the starting marker of the image link, not sure why +20 has been done though '''
start = pageResource.find(pattern)+20
''' This defines the end of the link, again not sure why +2 '''
end = pageResource.find("\"", start+2)
''' The link will be between start and end '''
imgLink = pageResource[start:end]
''' Link comes in a crooked format, the following converts into something we can make use of '''
imgLink=imgLink.replace("\\", "")         
''' The following downloads the file ''' 
urllib.urlretrieve(imgLink, name+".jpg")
''' Confirmation '''
print("Photo is successfully downloaded into the directory where your 500px.py file is.")

