import random

def coinTosses():
  heads=0;
  tails=0;
  print"Starting the program..."
  for i in range(1,5001):
    x_rounded = round(random.random())
    if (x_rounded==0):
      heads+=1
      print"Attempt #",i,": Throwing a coin... It's a head! .. Got",heads,"head(s) and",tails,"tail(s) so far"
    else:
      tails+=1
      print"Attempt #",i,": Throwing a coin... It's a tail! .. Got",heads,"head(s) and",tails,"tail(s) so far"
  print"Ending the program, thank you!"

coinTosses()
