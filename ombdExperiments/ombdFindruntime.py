import omdb

user_inp = raw_input("Print the name of the movie: ");
movie =omdb.title(user_inp)

print "Name of the country: ",movie.country
print "Total Votes: ",movie.metascore
print "Total Runtime: ",movie.runtime

