# myfile = open('myfile.txt')

# myfile = open('whoops_wrong.txt') # ERROR  wrong file name give 
# OR you don't know where is your .txt file(wrong path given)

# print(myfile.read())  #will read
# print(myfile.read())  #return 0 bcoz cursur is at the end.
# print(myfile.seek(0)) # to reset the cursur 
# print(myfile.read())  #will read again form beginning

# contents = myfile.read()
# print(contents)

# myfile.seek(0)
# print(myfile.readlines())

# myfile.close() # have to close file else sometimes error shows 
# or you could also do as below

# with open('myfile.txt') as my_new_file:
#   contents = my_new_file.read()
#   print(contents)

# with open('myfile.txt',mode = 'r') as myfile:
#   contents = myfile.read()
#   print(contents)

# with open('myfile.txt',mode = 'w') as myfile:
#   contents = myfile.read()
#   print(contents)  