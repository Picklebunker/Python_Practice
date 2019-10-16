import re
import random

def scramble(word):
  if len(word)<=3:
    return word
  else:
    i=[(l.start(0),l.end(0)) for l in re.finditer(r'[A-Za-z]',word)]
    start_i=i[0][0]
    end_i=i[-1][0]
    body=list(word[start_i+1:end_i])
    random.shuffle(body)
    result=word[start_i]+''.join(body)+word[end_i:]
    return result



text="""Write a Code that scrambles the words by following the rules below:
Words less than or equal to 3 characters need not be scrambled.
Don't scramble first and last char, so Scrambling can become Srbmnacilg or
Srbmnailcg or Snmbracilg , i.e. letters except first and last can be scrambled
in any order. Punctuation at the end of the word to be maintained as is i.e.
"Surprising," could become "Spsirnirug," but not "Spsirn,irug".
Following punctuation marks are to be supported - comma, question mark,
full stop, semicolon, exclamation. Do this for a file and
maintain sequences of lines."""

newtext=' '.join([scramble(w) for w in text.split()])

newtext
