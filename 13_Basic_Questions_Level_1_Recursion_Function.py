
##Recursion Function

'''
##1. Write a recursion program to print "Hello" till the system not show "out of memory error".
def print_till_error():
       print("hi............")
       print_till_error()

print_till_error()

##2. Write a recursion program to print "Hello" only 5 time.
def print_msg(num):
    
    if num<1:
        return 0
    print("Hello")
    print_msg(num-1)

print_msg(5)    

    
##3. Write a recursion program to print number 1 to 5.
print()
def print_1to5(num):
    if num > 5:
        return 0
    print(num)
    print_1to5(num+1)

print_1to5(1)

##4. Write a recursion program to print number from 11 to 18.
print()
def print_11to18(num):
    if num>18:
        return 0
    print(num)
    print_11to18(num+1)

print_11to18(11)    
##5. Write a recursion program to accept number from user and print sequence of that 
##number.
##--- e.g. input 11 and 15 ==> output 11 12 13 14 15.
print()
def seq_num(a,b):
    if a>b:
        return 0
    print(a)
    seq_num(a+1,b)
seq_num(1,15)    
    
##6. Write a recursion program to print the table of 2.
print()
def table_of_2(num):
        if num>10:
            return 0
        print(f"2*{num}=>",2*num)
        table_of_2(num+1)

table_of_2(1)        
    
##7. Write a recursion program to print the table of number given by user.
print()
def table_of_given_num(a,num=1):
    if num>10:
        return 0
    print(f"{a}*{num}=>",a*num)
    table_of_given_num(a,num+1)

table_of_given_num(int(input("Enter number to print table=>")))    

##8. Write a recursion function to print the table of 2 in reverse order.
print()
def rev_table_of_2(num):
    if num<=1:
        return 0
    print(f"2*{num}=>",2*num)
    rev_table_of_2(num-1)
    
rev_table_of_2(10)        

##9. Write a recursion function that ask 5 time the user name.
print()
def username_5times(num):
    if num<1:
        return 0
    user_name=input("Enter user name =>")
    print(user_name)
    username_5times(num-1)

username_5times(5)

##10. Write a recursion function to print the alphabets from "a" to "z".
print()
def print_a_z(a,b):
    if a>b:
        return 0
    print(chr(a))
    print_a_z(a+1,b)

x=ord("a")
y=ord("z")
print_a_z(x,y)   


##11. Write a recursion function to print the alphabets from "A" to "Z".
print()
def print_A_Z(a,b):
        if a>b:
            return 0
        print(chr(a))
        print_A_Z(a+1,b)
    
x=ord("A")
y=ord("Z")
print_A_Z(x,y)


##12. Write a recursion function to print each character of "Hello" one by one.
print()
def print_hello_chars(msg,l=0):
    if len(msg)<=l:
        return 0
    print(msg[l])
    print_hello_chars(msg,l+1)

print("Given=>Hello")    
print_hello_chars("Hello")
    


##13. Write a recursion function to print each element of a list ==> [1,4, 2, 6, "Hello"]
print()
def print_list_ele(list1,l=0):
    if len(list1)<=l:
        return 0
    print(list1[l])
    print_list_ele(list1,l+1)
list1 =[1,4, 2, 6, "Hello"]
print("Given =>",list1)
print_list_ele(list1)    
    
##14. Write a recursion function to print each element of a list in reverse order ==> [1,4, 2, 6,"Hello"]
print()
def reverse_list_ele(list1):
    if len(list1)==1:
        return list1
    print(list1[-1])
    return [list1[-1]]+reverse_list_ele(list1[:-1])

list1=[1,4,2,6,"Hello"]
print("\nGiven =>",list1)
print("each element of a list in reverse order=>")
data=reverse_list_ele(list1)
print(data)
##15. Write a recursion function to count the number of elements of a list ==> [1,4, 2, 6, "Hello"]

def count_list_ele(data):
       if data==[]:
              return 0
       
       return 1+count_list_ele(data[1::])
           
             
list1=[1,4, 2, 6, "Hello"]
print("\nGiven=>",list1)
x=count_list_ele(list1)
print(f"list {list1}: length is=>{x}")

##16. Write a recursion function to count each element in a "Hello world" string.

def string_index(msg,l=0):
       
       if len(msg)<=l:
              return 0
       if msg[l].isalpha():
              print(msg[l])
       string_index(msg,l+1)
       #print(f"index location= {l} of character => {msg[l]}")
             
msg = "Hello World"
print("\nGiven=>",msg)
string_index(msg)


##17. Write a recursion function to print length of each string in list ==>["King", "Naruto","Vijay", "King", "World", "Hello"]

def length_of_string(list1,l=0):
       #z={}
       if len(list1)<=l:
        return 0 
       x=list1[l]
       #print(""x)
       y=len(x)
       #z.update({x:y})
       print(f"length of string {x}=>",y)
       length_of_string(list1,l+1)    
       #print(z)
       
list1=["King", "Naruto","Vijay", "King", "World", "Hello"]
print("\nGiven=>",list1)
length_of_string(list1)


##18. Write a recursion function to print index location of each character of a string = "Hello, World"5.

def string_index(msg,l=0):
       if len(msg)<=l:
              return 0
       print(f"index location= {l} of character => {msg[l]}")
       string_index(msg,l+1)      

msg = "Hello, World"
print("\nGiven=>",msg)
string_index(msg)



##19. Write a recursion function to print index and value of each string in list ==> ["King","Naruto", "Vijay", "King", "World", "Hello"]

def list_string_index(msg,l=0):
       if len(msg)<=l:
              return 0
       print(f"index location=> {l} and value=> {msg[l]}")
       list_string_index(msg,l=l+1)
       
list1=["King","Naruto", "Vijay", "King", "World", "Hello"]
print("\nGiven=>",list1)
list_string_index(list1)

##20. Write a recursion function to print the ascii value of the string == > "King Naruto 12"

def print_ascii_of_string(msg,l=0):
       #z={}
       if len(msg)<=l:
              return 0
       x=ord(msg[l])
       print(msg[l],x)
       #z.update({msg[l]:x})
       print_ascii_of_string(msg,l=l+1)
       #print(z)       
msg="King Naruto 12"
print("\nGiven =>",msg)
print_ascii_of_string(msg)


##21. Write a recursion function that user for user name and password again and again till they 
##enter a right name and password.
##--- dictionaryOfUsername = {"user1": "pass123", "user2":"pass567"}

dictionaryOfUsername = {"user1": "pass123", "user2":"pass567"}

def validate_user_detail(user_data):
       user_name=input("Enter user_name =>")
       password =input("Enter password =>")

       if user_name in user_data and password in user_data.get("user1"):
              print("User data matched...")
              return 0
       validate_user_detail(user_data)      

validate_user_detail(dictionaryOfUsername)      


##22. Write a recursion function to calculate a sum of 1 to 9.
num_sum=0
def sum_1to9(n):
      
       if n==0:
              return 0
       print(n)
       return n+sum_1to9(n-1)

x=sum_1to9(9)      
print("sum of 1 to 9 =>",x)


##23. Write a recursion function that accept the number from user and print the sum of 1 to n 
##(here n is user given number).

def sum_of_n_numbers(n):
       if n==0:
              return 0
       print(n)
       return n+sum_of_n_numbers(n-1)
              
num=int(input("\nEnter no "))
print(f"numbers from 1 to {num}=>")
x=sum_of_n_numbers(num)
print(f"sum of 1 to {num}=>",x)


##24. Write a recursion function to calculate the factorial of 5.
def fact(n,s=1):
       if n<=1:
              return s
       s=s*n
       return fact(n-1,s)

x=fact(5)
print(f"factorial of 5=>",x)


##25. Write a recursion function that accept number from user and calculate it's factorial.
def fact_num_user(n,s=1):
       if n<=1:
              return s
       s=s*n
       return fact_num_user(n-1,s)
num=int(input("Enter number to find factorial=>"))
x=fact_num_user(num)
print(f"factorial of {num} is=>",x)


##26. Write a recursion function to print the 10th fibonacci number.
def fibo_10_position(n):
              if n==1:
                     return 0
              elif n==2:
                     return 1
              else:
                     return fibo_10_position(n-1)+ fibo_10_position(n-1)
fib=fibo_10_position(10)              
print("the 10th fibonacci number is =>",fib)

##27. Write a recursion function that accept input as number (i.e. index location of fibonacci 
##number) and print that fibonaci number.

def fibo_10_position(n):
              if n==1:
                     return 0
              elif n==2:
                     return 1
              else:
                     return fibo_10_position(n-1)+ fibo_10_position(n-1)
num=int(input("Enter position to find fibonacci number=>"))
fib=fibo_10_position(num)              
print(f"the {num} fibonacci number is =>s",fib)


'''
##28. Write a recursion function to reverse a number using Recursion.

def reverse_num(n,l=1):
    if len(str(n))<0:
        return n
    return n[-1]+reverse_num(n[:-1])
    
print(reverse_num(654231))
##
##
## if len(str(n))<l:
##              return 0
##       nlen=len(str(n))
##       num=str(n)
##       x=num[nlen-l]
##       reverse_num(n,l+1)
##       print(x)
##
##




