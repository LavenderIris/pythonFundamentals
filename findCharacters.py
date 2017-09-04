def findChar(words, char):
  new_list=[];
  for word in words:
    if (word.find(char)>-1):
      new_list.append(word)
  print new_list

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
findChar(word_list, char)