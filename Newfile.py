with open('myNewFile.txt', mode = 'r') as f:
  print(f.read())

with open('myNewFile.txt', mode = 'a') as f:
  f.write('\nFOUR ON FOURTH') 
with open('myNewFile.txt', mode = 'r') as f:
  print(f.read())  

with open('Hahahhaha.txt', mode = 'w') as f:
  f.write('I CREATED THIS FILE!')

with open('Hahahhaha.txt', mode = 'r') as f:
  print(f.read())  