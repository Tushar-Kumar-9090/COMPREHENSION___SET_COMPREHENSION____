

## Set comprehension syntax with one value and one for loop:-
#* Adding the numbers into the Set by normal approach:-
s=set()
for i in range(1,11):
    s.add(i)
print(s)





#* Adding the numbers into the Set by Set comprehension:-
l={i for i in range(1,11)}
print(l)






#* Adding the squares numbers into the Set by Set comprehension:-
l={i**2 for i in range(1,11)}
l={i*i for i in range(1,11)}
print(l)






## Set comprehension syntax with one value and one for loop and one if condition:-
#* Adding the even numbers into the Set by normal approach:-
s=set()
for i in range(1,11):
    if i%2==0:
        s.add(i)
print(s)






#* Adding the even numbers into the Set by Set comprehension-
l={i for i in range(1,11) if i%2==0}
print(l)





## Set comprehension syntax with one value and one for loop and multiple if condition:-
#* from the given tuple add only even numbers which are greater than 50 into the Set in normal approach:-
t=(11,78,34,23,67,90,70)
s=set()
for i in t:
    if i%2==0 and i>50:
        s.add(i)
print(l)






#* from the given tuple add only even numbers which are greater than 50 into the Set in Set comprehension:-
t=(11,78,34,23,67,90,70)
l={i for i in t if i%2==0 and i>50}
print(l)






#* from the given tuple add even numbers and odd numbers which are greater than 30 in Set comprehension:-
t=(11,78,34,23,67,90,70)
l={i for i in t if i%2==0 or i>30}
print(l)






## Set comprehension syntax with one value and one for loop and one if-else condition:-
#* Adding 1 in even position and 0 in odd position
t=(11,22,100,23,44,60)
l={1 if i%2==0 else 0 for i in t}
print(l)





#* if it is non-negetive and more than 5:-
l=(1,2,3,-99,55,66,-100,5)
l1={i for i in l if i>0 and i>5}
print(l1)