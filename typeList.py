def typeList(list):
  # seed the first item's type 
  my_type=type(list[0])
  prev_type=my_type
  str_list=""
  sum=0

  for item in list:
    my_type=type(item)
    if my_type is not prev_type:
        my_type="mixed"
    if type(item) is str:
      str_list+=" "+item  
    elif type(item) is int:
      sum+=item
    elif type(item) is float:
      sum+=item
    prev_type=my_type

  # output section
  if (my_type is int):
    my_type="integer"
  elif (my_type is str):
    my_type="string"
  


  def typeList2(list):
  # seed the first item's type 
  str_list=""
  sum=0

  for item in list:
    if type(item) is str:
      str_list+=" "+item  
    elif type(item) is int:
      sum+=item
    elif type(item) is float:
      sum+=item

  if (sum) and (str_list):
    print("The list you entered is of mixed type")
    print"String:", str_list
    print"Sum: ", sum
  elif (str_list):
    print("The list you entered is of string type")
    print"String:",str_list
  else:
    print("The list you entered is of integer type")
    print"Sum:", sum
  
  print("The list you entered is of "+my_type+" type")
  if(str_list):
    print("String:"+str_list)
  if (sum):
    print("Sum: "+str(sum))
      
l = ['magical unicorns',19,'hello',98.98,'world']
typeList(l)
l = ['magical unicorns',19,'hello',98.98,'world']
