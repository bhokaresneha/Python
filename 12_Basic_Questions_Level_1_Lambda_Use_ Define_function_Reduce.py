##Lambda/ User Define and Reduce.
from functools import reduce

##23. Write a program to find the minimum value of given list.
##--- list1 = [ 23, 13, 45, 23, 9, 87]
y=lambda a,b:a if a<b else b   
list1 = [ 23, 13, 45, 23, 9, 87]
print("\nGiven",list1)
min_val=reduce(y,list1)
print(min_val)

##24. Write a program to find the max value of given list.
##--- [ 23, 13, 45, 23, 9, 87]

y=lambda a,b:a if a>b else b   
list1 = [ 23, 13, 45, 23, 9, 87]
print("\nGiven",list1)
mix_val=reduce(y,list1)
print(mix_val)

##25. Write a program to find the largest even number from the list.
##y=lambda a,b:a if a%2==0 and a>b else b   
##list1 = [ 24, 13, 45, 23, 9, 87]
##print("\nGiven",list1)
##mix_val=reduce(y,list1)
##print(mix_val)

##26. Write a program to calculate the sum of all the number in a list.

y=lambda a,b:a+b
list1 = [ 23, 13, 45, 23, 9, 87]
add=reduce(y,list1)
print(add)

##27. Write a program to find the string whose length is greater than others.
##--- list1 = ["Hello", "king", "Python", "Java", "coding"]

y=lambda a,b:a if len(a)>=len(b) else b   
list1 = ["Hello", "king", "Python", "Java", "coding"]
print("\nGiven",list1)
mix_len=reduce(y,list1)
print(mix_len)

##28. Write a program to find the character whose ascii value is greater among all
##--- list1 = ['2', '0', "a", "2", "3", "@", '2']

y=lambda a,b:a if ord(a)>=ord(b) else b   
list1 = ['2', '0', "a", "2", "3", "@", '2']
print("\nGiven",list1)
mix_ascii_len=reduce(y,list1)
print(mix_ascii_len)

##29. Write a program to find the character whose ascii value is smallest among all
##--- list1 = ['2', '0', "a", "2", "3", "@", '2']

y=lambda a,b:a if ord(a)<=ord(b) else b   
list1 = ['2', '0', "a", "2", "3", "@", '2']
print("\nGiven",list1)
min_ascii_len=reduce(y,list1)
print(min_ascii_len)

##30. Write a program to merge the 3 list.
##--- list1 = [2, 3,4,5], list2 = [12, 13, 14, 14], list3 = [90, 89, 78, 67]

list1 = [2, 3,4,5]
list2 = [12, 13, 14, 14]
list3 = [90, 89, 78, 67]




