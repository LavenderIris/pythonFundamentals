my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dict2Tuples(my_dict):
  output=[]
  for key, value in my_dict.iteritems():
    output.append((key, value))
  print output
  return output
    
dict2Tuples(my_dict)