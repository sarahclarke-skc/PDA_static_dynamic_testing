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
    # == instead of =
    if card.value = 1:
      return True
      # missing : after else 
    else
      return False
   
# spelling error - dif instead of def
# need , between the parameters
  dif highest_card(self, card1 card2):
  # indentation error
  if card1.value > card2.value:
    # card1 instead of card in line 33
    return card
  else:
    return card2
  

# total variable hasn't been set, should be total = 0 in line 42
#indent error

def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    # return indentation wrong 
    # return statement needs to be in f string {total}
    return "You have a total of" + total
  
```
