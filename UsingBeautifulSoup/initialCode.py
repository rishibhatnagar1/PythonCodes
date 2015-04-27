import requests
from bs4 import BeautifulSoup
''' Going to attempt to scrape data from 500 px '''
link = "https://500px.com/photo/106624697/droplet-by-usagi-moti?from=popular&only=Macro"
''' Make a request to the link to get all the source code '''
r = requests.get(link)
''' The source code can be viewed using r.content, we give it as an input to BeautifulSoup '''
soup = BeautifulSoup(r.content)
''' We could print this using the following command '''
#print soup.prettify()
''' Find the position of the image, the following gives the script which has the image in it '''
g_data = soup.find_all("script",{"type":"application/ld+json"})
print g_data

''' Not able to find out how to reach the image inside the json script '''
