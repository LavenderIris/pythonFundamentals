the_dict={
      "name":"Anna",
      "age": 101,
      "country":"The United States",
      "language":"Python"
      }

def readDict(dict):
  print "My name is",dict["name"]
  print "My age is",dict["age"]
  print "My country of birth is",dict["country"]
  print "My favorite language is",dict["language"]
  
readDict(the_dict)