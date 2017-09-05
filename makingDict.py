def makingDict(arr1, arr2):
  my_dict={}
  keys=[];
  values=[]
  if (len(arr1)>=len(arr2)):
    keys=arr1
    values=arr2
  else :
    keys=arr2
    values=arr1
    
  for i in range(len(keys)):
    # if a value exists
    if i <= len(values)-1 :
      my_dict[keys[i]]=values[i]
    else:
      my_dict[keys[i]]=None
  print(my_dict)
  
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins","llamas"]
makingDict(name, favorite_animal)