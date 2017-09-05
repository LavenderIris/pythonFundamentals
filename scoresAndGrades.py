import random

def scoresAndGrades():
  print"Scores and Grades"
  for i in range(10):
    score=random.randint(60, 100)
    if score>=90 and score<=100:
      print"Score",score,"Your grade is A"
    elif score>=80:
      print"Score",score,"Your grade is B"
    elif score>=70:
      print"Score",score,"Your grade is C"
    elif score>=60:
      print"Score",score,"Your grade is D"
  print"End of the program. Bye!"
  
scoresAndGrades()