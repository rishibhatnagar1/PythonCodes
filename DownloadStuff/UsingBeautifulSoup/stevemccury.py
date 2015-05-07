import requests
from bs4 import BeautifulSoup
import time

''' Going to attempt to download images from Steve McCurry, that come in as google image search '''
''' Google won't let you scrape the data. FYI '''
link =raw_input("Please Drop link of the gallery here: ")
name = raw_input("Name it: ")
''' Make a request to the link to get all the source code '''
r = requests.get(link)
''' The source code can be viewed using r.content, we give it as an input to BeautifulSoup '''
soup = BeautifulSoup(r.content)
''' We could print this using the following command '''
#print soup.prettify()
''' Find the position of the image, the following gives the script which has the image in it '''
g_data = soup.find_all("a")
#print g_data
''' Save Image '''
count = 0 #This will help in saving the files with an index
def saveImage(dlink):
        res =requests.get(dlink)
        if res.status_code == 200:
                    with open(name+str(count)+".jpg", 'wb') as f:
                        for chunk in res.iter_content():
                            f.write(chunk)

''' The img tags will have attributes which need to be accessed, they can be using .attrs[""] we do not need to go and look for the application/json at the bottom of the page '''
for aTag in g_data:
	if "href" in aTag.attrs and "photos" in aTag.attrs["href"]:
		#print aTag.attrs["href"]
		count +=1
		dlink = aTag.attrs["href"]
		saveImage(dlink)
		print "."
count = 0
print "All images saved"
