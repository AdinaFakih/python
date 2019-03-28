# mylist = [1,2,3]
# mylist.append(4)
# print(mylist)
# print(mylist.pop())

# help(mylist.insert)

# def name_function():
#   '''
#   DOCSTRING: INFO
#   INPUT: no input
#   OUTPUT: hello
#   '''
#   print("hello")

# help:name_function

# def say_hello(name='NAME'):
#   print('hello ' + name)

# say_hello('adina')
# say_hello()

# def say_hello(name='NAME'):
#   return 'hello ' + name

# result = say_hello('adi')
# print(result)

# def add(n1,n2):
#   return n1+n2

# result=add(20,30)
# print(result)

# def dog_check(mystring):
#   if dog in mystring.lower():
#     return True
#   else:
#     return False

# print(dog_check('Dog run way'))

# def dog_check(mystring):
#   return 'dog' in mystring.lower()
# print(dog_check('Dog run way'))
# ###'dog' in 'dog ran way'

def pig_latin(word):
  first_letter = word[0]
  #check if vowel
  if first_letter in 'aeiou':
    pig_word = word + 'ay'
  else:
    pig_word = word[1:] + first_letter + 'ay'
  return pig_word
print(pig_latin("word"))