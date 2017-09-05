students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names1(s):
  for obj in s:
    print obj['first_name'], obj['last_name']

names1(students)


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def names2(users):
  count=1
  print "Students"
  for students in users["Students"]:
    length = len(students["first_name"]) + len(students["last_name"])
    print count,'-',students["first_name"].upper(), students["last_name"].upper(),'-', length
    count+=1
  print "Instructors"
  count=1
  for instructor in users["Instructors"]:
    length = len(instructor["first_name"]) + len(instructor["last_name"])
    print count,'-',instructor["first_name"].upper(), instructor["last_name"].upper(),'-', length
    count+=1

names2(users)
  