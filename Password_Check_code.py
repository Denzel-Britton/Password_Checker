#testing connection to get hub

import string
#string.ascii_uppercase returns all alphabet in upper case
#comprehension list [ part1   part2  part3] ----> break it down start part 3 and work backwards   [ transformation(item in are new list ,for var in ,orginal_list]

#  if uppercase letter is found it will add a 1 to c  else c = 0 this  iterates through each char
psswd = "Helloword"
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in psswd])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in psswd])
special_char = any([1 if c in string.punctuation else 0 for c in psswd])
digits = any([1 if c in string.digits else 0 for c in psswd])

print(upper_case)
characters= [upper_case,lower_case,special_char,digits]

length= len(psswd)
# setting paramaters for the scoring of the password
score = 0

if length > 8:
    score += 1
if length > 12:
    score += 1
if length >17:
    score += 1
if length > 20:
    score += 1

# will to query common password list. with filetype:txt
#stopping point