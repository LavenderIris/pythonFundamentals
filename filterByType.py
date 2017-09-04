def filterByType(arg):
  if isinstance(arg,int):
    bigger(arg)
  elif isinstance(arg,str):
    stringLength(arg)
  elif isinstance(arg,list):
    listLen(arg)


def bigger(num):
  if (num>=100):
    print("That's a big number!")
  else:
    print("That's a small number")
    
def stringLength(str):
  if (len(str)>=50):
    print("long sentence")
  else:
    print("Short sentence")

def listLen(list):
  if (len(list)>=10):
    print "Big list!"
  else:
    print("Short List")



sI = 45
mI = 100
bI = 455
eI = 0
spI = -23

filterByType(sI)
filterByType(mI)
filterByType(bI)
filterByType(eI)
filterByType(spI)

sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""

filterByType(sS)
filterByType(mS)
filterByType(bS)
filterByType(eS)

aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

filterByType(aL)
filterByType(mL)
filterByType(lL)
filterByType(eL)
filterByType(spL)
