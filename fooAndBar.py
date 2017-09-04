def isPerfectSquare(num):
  return (int(num**(0.5))**2) == num
    
def isPrime(num):
  for n in range(2, num):
    if num%n==0:
      return False
  return True

def fooAndBar():
  for n in range(100,100001):
    output=""
    if (isPrime(n)):
      output+="Foo"
    elif (isPerfectSquare(n)):
      output+="Bar"
    else:
      output="FooBar"
    print n, output
      

fooAndBar()