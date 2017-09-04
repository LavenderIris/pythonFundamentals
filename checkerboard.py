def checkerboard():
  stars="* * * *"
  for i in range(8):
    if(i%2==1):
      print" "+stars
    else:
      print stars
      
checkerboard()