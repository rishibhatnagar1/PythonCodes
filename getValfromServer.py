import requests 

link ="http://secure-anchorage-4352.herokuapp.com/numberGet"

def makeGetreq():
    r = requests.get(link)
    curValue = r.text
    if curValue == "none":
        return None
    else:
        return curValue 

x = makeGetreq()
print x
