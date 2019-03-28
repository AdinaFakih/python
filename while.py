# x = 0
# while x < 5:
#   print(f'the current value of x is {x}')
#   x = x + 1
#   x += 1
# else:
#   print('X is not less than 5')

# x = [1,2,3]
# for item in x:
#   pass

# print('end of my script')

# mystring = 'sammy'
# for letter in mystring:
#   print(letter)

# mystring = 'sammy'
# for letter in mystring:
#   if letter == 'a':
#     continue
#   print(letter)

mystring = 'sammy'
for letter in mystring:
  if letter == 'a':
    break
  print(letter)

x = 0
while x < 5:
  if x == 2:
    break
  print(x)
  x+=1