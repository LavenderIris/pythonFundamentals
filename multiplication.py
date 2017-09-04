def multiplication():
  top=range(1,13)
  top_str="x"
  
  for t in top:
    top_str+='%4s'%t
  print(top_str)
  
  mult_str="x"
  for y in range(1,13):
    mult_str=str(y)
    for x in range(1,13):
      mult_str+='%4s' % str(x*y)
    print(mult_str)
    mult_str=""
  
multiplication()