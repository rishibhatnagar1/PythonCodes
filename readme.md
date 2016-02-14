#Python Codes
Setting up a space for storing all the codes I keep working on. Nothing specific here, it is a collection of all the hacks I keep working on.



####Structuring Data 

This has been one of the interesting learning I have had in the past few days. I was able to scrape the data or get it from APIs but structuring it was still difficult. Was able to structure data this week at work. Here is how I did it.

Step 1.Open a file to write to :

`fo = open("dataRevAll.txt", "wb")`

Step 2.Define the headers for the file:

`fo.write(str("Product ID"+"|"+"Content"+"|"+"Average Rating"+"|"+"Rating By User"+"|"+"Helpful Votes")+ str(os.linesep))`

Step 3.Structure the data in the loop after scraping:
`fo.write(str(id+"|"+content+"|"+ratingAvg+"|"+ratingUser))`

Where all the above variables will have values coming from API. 

####Undestanding delimiter
I have used | as the delimiter here. What happens is the data is limited by this. So you could open a .txt file in excel and click on a column "A" , go to `Data` in MS Excel and then select `text to columns` . Chose `delimited` as the option there. Click `next` and then chose `other` option, write `|` in the delimiter.
Once you click on `Finish`, you will be able to see the data structured beautifully.

####Python VirtualEnv
Installation: `$ pip install virtualenv`

Here is the documnetation on [how](http://docs.python-guide.org/en/latest/dev/virtualenvs/) it works.


###ToDo
<li>MQTT is yet to be tested.</li>
<li>Need to experiment on iPython Notebooks. Find out what they are and where they should /could be used.</li>
<li>Find out how to implement CoAP using python.</li>
<li>Find out if there is a module for ESP8266 for python</li>
####Updates
<li>Added omdb.</li>

###Random learnings

*I always confuse between how objects should be handeled in python and JS. In JS , a dot has to be used to access various things. In Python how ever [] have to be used to access the key value pairs.

*Installed MacVim today and love it.[This] (https://github.com/macvim-dev/macvim) is to be clone and then [this](https://github.com/macvim-dev/macvim/blob/master/README_mac.txt) is to be followed.

*For making the syntax on easily, just type `:syntax on` and you are done.



