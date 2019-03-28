r = (10**2)+(0.02*10+0.05)
print(r)

a = 4*(6+5)
print(a)

a = 4*6+5
print(a)

a = 4+6*5
print(a)

print(type(3+1.5+4))

s = 'hello'
print(s[1])
print(s[::-1])
print(s[4])
print(s[-1])

list1 = [0,0,0]
list2 = [0]*3
list3 = [1,2,[3,4,'hello']]
print(list3[2][2])
list3[2][2] = 'goodbye'
print(list3)
list4 = [5,3,4,6,1]
list4.sort()
print(list4)
sorted(list4)

d = {'simple_key':'hello'}
print(d['simple_key'])
d = {'k1':{'k2':'heLLo'}}
print(d['k1']['k2'])
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))