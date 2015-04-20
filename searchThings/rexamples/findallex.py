'''This is similar to split(). Findall accepts a pattern that indicates which string store turn in a list. It is like split() but we specify matching parts, not delimiters.
We scan a string for all words starting with the letter d or p, and with one or more following word characters. '''
import re

# Input.
value = "You know this is a rather interesting topic because dat dictator is not holding a dictionary to dictate abc 123 def 456 dot map pat"

# Find all words starting with d or p.
list = re.findall("[dp]\w+", value)

# Print result.
print(list)

'''Pattern: [dp]\w+

[dp]     A lowercase d, or a lowercase p.
\w+      One or more word characters. '''
