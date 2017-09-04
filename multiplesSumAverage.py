def multiples1():
  for i in range(1, 1000, 2):
    print(i)
    
def multiples2(){
  for i in range(5,1000000,5):
    print(i)
}

def sumList(list):
  sum=0
  for num in list:
    sum+=num
  print("sum: "+str(sum))
  
def avg(list):
  sum=0
  for num in list:
    sum+=num
  print("average: "+str(sum/len(list)))

multiples1()
multiples2()
a = [1, 2, 5, 10, 255, 3]
sumList(a)
avg(a)