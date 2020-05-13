from random import  randint
def array_diff(a,b):
    return [item for item in a if item not in b]
# My shitty solution :/
#    for i in b:
#        x = True
#        while (x):
#            if i in a:
#                a.remove(i)
#            else: 
#                x = False      
#    
#    return a

alen,blen=randint(0,20),randint(0,20)
a=[randint(0,40)-20 for i in range(alen)]
print("a was: ")
print(a)
b=[randint(0,40)-20 for i in range(blen)]
print("b was: ")
print(b)

a = array_diff(a,b)


print("a is: ")
print(a)