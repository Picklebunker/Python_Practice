import re

def condense(string):
  result=""
  for s in string.split():
    result+=s.capitalize()
  return result

def vaporize(string2):
  components= re.sub( r"([A-Z])", r" \1", string).split()
  result=components[0]
  for c in components[1:]:
    result+=" "+c
  return result





string="My name is someone"
string2=condense(string)

print(condense(string))
print(vaporize(string))
