def compareLists(list1, list2):
  if (len(list1)!=len(list2)):
    print("The lists are not the same")
    return
  
  for i in range(len(list1)):
    if list1[i]!=list2[i]:
      print("The lists are not the same")
      return
  print("The lists are the same")

def compareLists2(list1, list2):
  if (list1!=list2):
    print("The lists are not the same")
  else:
    print("The lists are the same")
 
  
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compareLists(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
compareLists(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
compareLists(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
compareLists(list_one, list_two)