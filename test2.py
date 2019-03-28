# st = 'print only the words that start with s in this sentence'
# for word in st.split():
#   if word[0] == 's':
#     print(word)

# print(list(range(0,11,2)))

# for num in range(0,11):
#   if num%2==0:
#     print(num)

# print([x for x in range(1,51) if x%3 == 0])

# for num in range(1,50):
#   if num%3 == 0:
#     print(num)

# st ='print every word in this sentence that has an even number of letters'
# for word in st.split():
#   if len(word)% 2==0:
#     print(word + ' is even')

for num in range(1,101):
  if num%3 == 0 and num%5 == 0:
    print('fizzbuzz')
  elif num%3 == 0:
    print('fizz')
  elif num%5 == 0:
    print('Buzz')
  else:
    print(num)

st = 'create a list of the first letters of every word in this string'
print([word[0] for word in st.split()])