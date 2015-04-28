import requests
from bs4 import BeautifulSoup
''' Going to attempt to download images from Steve McCurry, that come in as google image search '''
''' Google won't let you scrape the data. FYI '''
link ="" # try with steve mccurry's website
#name = raw_input("Name it: ")
''' Make a request to the link to get all the source code '''
r = requests.get(link)
''' The source code can be viewed using r.content, we give it as an input to BeautifulSoup '''
soup = BeautifulSoup(r.content)
''' We could print this using the following command '''
#print soup.prettify()
''' Find the position of the image, the following gives the script which has the image in it '''
g_data = soup.find_all("a")
#print g_data
''' The img tags will have attributes which need to be accessed, they can be using .attrs[""] we do not need to go and look for the application/json at the bottom of the page '''
for aTag in g_data:
	if "href" in aTag.attrs: 
#and "rg_l" in aTag.attrs["class"]:
		print aTag.attrs
		#dlink = aTag.attrs["src"]
'''Retrieve image '''
#ires =requests.get(dlink)
#if res.status_code == 200:
#    with open(name+".jpg", 'wb') as f:
#        for chunk in res.iter_content():
#            f.write(chunk)
 
