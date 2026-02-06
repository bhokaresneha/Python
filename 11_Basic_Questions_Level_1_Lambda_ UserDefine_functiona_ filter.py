##Lambda/ User Define function and filter

##16. Write a function to find the all even number in a list or tuple.
##i. --- list1 = [ 1, 22, 33, 24, 56]
list1 = [ 1, 22, 33, 24, 56]
def even_num(list1):
        if list1%2==0:
            return 1
        else:
            return 0
print("\nGiven=>",list1)
x=list(filter(even_num,list1))
print("all even number in a list or tuple => ",x)

##17. Write a function to find all the odd number in the list or tuple.
##i. --- list1 = [ 3, 4, 2, 6, 3, 1]
list1 = [ 3, 4, 2, 6, 3, 1]
def odd_num(num):
    if num%2!=0:
        return 1
    else:
        return 0

print("\nGiven=>",list1)
odd=list(filter(odd_num,list1))
print("all the odd number in the list or tuple=>",odd)

##18. Write a function to find all the numbers who are all divisible of 5
##i. --- list1 = [23, 45, 40, 23, 25]
list1 = [23, 45, 40, 23, 25]
def div_by5(num):
    if num %5==0:
        return 1
    else:
        return 0
print("\nGiven=>",list1)    
x=list(filter(div_by5,list1))
print("all the numbers who are all divisible of 5=>",x)

##19. Write a function to find all the word whose length is even.
##i. --- list1 = ["Hello", "king", "of", "Jungle", "Tiger"]
list1 = ["Hello", "king", "of", "Jungle", "Tiger"]
def length_even(w):
    
    if len(w)%2==0:
        return 1
    else:
        return 0
print("\nGiven=>",list1)
x=tuple(filter(length_even,list1))
print("all the word whose length is even=>",x)

##20. Write a function to find all the word whose last letter is a vowel
##i. --- list1 = ["Hello", "king", "of", "Junge", "Tiger"]
list1 = ["Hello", "king", "of", "Junge", "Tiger"]

def last_letter_vowel(word):
    if word[:-2:-1]=="a" or word[:-2:-1]=="e" or word[:-2:-1]=="i" or word[:-2:-1]=="o" or word[:-2:-1]=="u":
        return 1
    else:
        return 0
    
print("\nGiven=>",list1)
vowel=list(filter(last_letter_vowel,list1))
print("all the word whose last letter is a vowel=>",vowel)

##21. Write a function to find all the number which are comes in table of 11.
##i. --- list1= [11, 22, 234, 445, 121]
list1= [11, 22, 234, 445, 121]

def table_11(list1):
        if list1%11==0:
                return 1
        else:
                return 0

print("\nGiven=>",list1)        
x=list(filter(table_11,list1))
print("all the number which are comes in table of 11=>",x)
##22. Write a function to find all the palindrome number from the list.
##i. --- list1 = [11, 23, 121, 212, 909]

list1 = [11, 23, 121, 212, 909]
def palindrome(val):
                if str(val)==str(val)[::-1]:
                        return 1
                else:
                        return 0
 
print("\nGiven =>",list1)
x=list(filter(palindrome,list1))
print("all the palindrome number from the list=>",x)


