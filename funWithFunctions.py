def oddEven():
  for i in range(1,2001):
    if (i%2==1):
      print"Number is",i,"This is an odd number."
    else:
      print"Number is",i,"This is an even number."
      
      
def multiply(arr,num):
  for i in range(len(arr)):
    arr[i]*=num
  return arr
  
  
def layered_multiples(arr):
  new_array=[]
  for i in range(len(arr)):
    new_array.append([1]*arr[i])
  return new_array
  
  
a = [2,4,5]
b = multiply(a, 3)
print b

x = layered_multiples(multiply([2,4,5],3))
print x