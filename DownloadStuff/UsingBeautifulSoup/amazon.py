import requests
from bs4 import BeautifulSoup
import time

link ="http://www.amazon.com/Fitbit-Wireless-Activity-Sleep-Wristband/dp/B00BGO0Q9O/ref=sr_1_1?s=wearable-tech&ie=UTF8&qid=1432541968&sr=1-1&keywords=fitbit#customerReviews"

''' Make a request to the link to get all the source code '''
r = requests.get(link)
''' The source code can be viewed using r.content, we give it as an input to BeautifulSoup '''
soup = BeautifulSoup(r.content)
''' We could print this using the following command '''
print soup.prettify()
''' Find the position of the image, the following gives the script which has the image in it '''
#g_data = soup.find_all("img")
