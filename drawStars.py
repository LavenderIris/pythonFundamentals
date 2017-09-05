def draw_stars(list):
  for x in list:
    print '*'*x
    
def draw_stars2(list):
  for x in list:
    if (type(x)==int):
      mystr='*'*x
    elif (type(x)==str):
      mystr=x[0].lower()*len(x)
    print(mystr)

x = [4, 6, 1, 3, 5, 7, 25]
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars2(x)
