###Structuring Data 

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




Just for the sake of fun, want to write a script that could scan for all the images and videos in a webpage, give the total number of them, and give an option of dowloading them.
It does not work for 500px prime though.
Codeschool script has been writter by [sindhus](https://github.com/sindhus). Thanks to her. She is awesome!


 
