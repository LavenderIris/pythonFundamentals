def findAndReplace(words):
  index=words.find('day');
  words=words.replace("day","month", 1);
  print("Index of the word day: " + str(index))
  print(words)
  
# function run here

def minAndMax(list):
  print("Max is: "+ str(max(list)))
  print("Min is: "+ str(min(list)))

def firstAndlast(list):
  print("first and last of array: "+ list[0] + " "+ list[-1])
  
def newList(list):
  list=sorted(list)
  count=len(list)/2
  temp=list[:count]
  
  for i in range(count-1):
    list.pop(0)
  list[0]=temp
  print(list)
  return list

w = "It's thanksgiving day. It's my birthday,too!"
findAndReplace(w)

x = [2,54,-2,7,12,98]
minAndMax(x)

y = ["hello",2,54,-2,7,12,98,"world"]
firstAndlast(y)

z = [19,2,54,-2,7,12,98,32,10,-3,6]
newList(z)

