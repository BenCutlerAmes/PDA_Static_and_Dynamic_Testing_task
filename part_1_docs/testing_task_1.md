### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #missing equals sign for logical test. Should be ==
      return True
    else      # Missing colon after else
      return False
   

  dif highest_card(self, card1 card2): # def misspelled and missing a comma between card1 and card2
  if card1.value > card2.value: ##indentation incorrect
    return card
  else:
    return card2
  


def cards_total(self, cards):
  total   # missing = to define as variable
  for card in cards:
    total += card.value
    return "You have a total of" + total  # return inside the for loop and total won't concatenate unless coerced to string
    
  
```
