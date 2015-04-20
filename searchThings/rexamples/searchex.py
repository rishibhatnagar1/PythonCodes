''' Search attempts to find a pattern at all possible starting points in the string, Match just stries the first starting point. That is the major difference '''
import re

# Input.
value = "bloddyvoceferiouslyvivaciousvivaldivoorheesville"
''' Lower case characters v and i together , .* - zero or more characters of anytype '''
m = re.search("(vi.*)", value)
if m:
    # This is reached.
    print("search:", m.group(1))

m = re.match("(v\w+12\v)", value)
if m:
    # This is not reached.
    print("match:", m.group(1))

