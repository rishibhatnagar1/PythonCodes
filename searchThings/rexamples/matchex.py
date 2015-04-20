''' Program gets an input. We use re.match in a for loop. We use .groups(), which returns a tupleof the text contained, which was matched. '''
import re

# Sample strings.
list = ["dog dot", "do don't", "dumb-dumb", "no match"]

# Loop.
for element in list:
    # Match if two words starting with letter d.
    ''' d means lower case of d , \w is word character, + means one more , \W means a non word ch    aracter '''
    m = re.match("(d\w+)\W(d\w+)", element)
    print element
    # See if success.
    if m:
        print(m.groups())

