'''
#Quetion-1. Area of a Triangle: Write a Python program to calculate the area of a triangle given its base and height.
               #Formula: Area = (base × height) / 2

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = (base * height) / 2
print("The area of the triangle is:", area)

#Output=>Enter the base of the triangle: 5
Enter the height of the triangle: 5
The area of the triangle is: 12.5


#Quetion-2. Write a Python program to calculate the perimeter of a square.
            #Formula: Perimeter = 4 * side

side = int(input("Enter the side of the square: "))
perimeter = 4 * side
print("The perimeter of a square is:",perimeter)
#Output=>
Enter the side of the square: 4
The perimeter of a square is: 16


#Quetion-3. Area of a Rectangle: Write a Python program to calculate the area of a rectangle given
        #its length and width.
    #Formula: Area = length × width

length=int(input("Enter the Length of rectangle: "))
width=int(input("Enter the width of rectangle: "))
area = length * width
print("The area of the rectangle is:", area)   

#Output=>Enter the Length of rectangle: 5
Enter the width of rectangle: 5
The area of the rectangle is: 25

#Quetion-4.Volume of a Cube: Write a Python program to calculate the volume of a cube given its side length.
    #Formula: Volume = side length^3

side_length=int(input("Enter the side_length of cube: "))
volume = side_length **3 
print("The volume of a cube:", volume)
#Output=>
Enter the side_length of cube: 5
The volume of a cube: 125

#Quetion-5. Simple Interest Calculator:Write a Python program to calculate the simple interest given
        #the principal amount, interest rate, and time period.
    #Formula: Simple Interest = (principal × rate × time) / 100
    
principle_amount=float(input("Enter the principle Amount:"))
interest_rate=float(input("Enter the Simple Interest Rate:"))
time=float(input("Enter the Time:"))

simple_interest=(principle_amount * interest_rate * time) / 100
print("Simple interest is ",simple_interest)

#Output=>Enter the principle Amount:2000
Enter the Simple Interest Rate:2
Enter the Time:2
Simple interest is  80.0


#Quetion-6. Speed Calculator: Write a Python program to calculate the speed given the distance and time.
        #Formula: Speed = distance / time

distance=float(input("Enter the Distance"))
time=float(input("Enter the time"))

speed=distance/time
print("Speed is:",speed)

#Output=>Enter the Distance50
Enter the time5
Speed is: 10.0

#Quetion-7. Area of a Trapezoid: Write a Python program to calculate the area of a trapezoid given its bases and height.
    #Formula: Area = (1/2) × (base1 + base2) × height

base1=float(input("Enter the value of base1"))
base2=float(input("Enter the value of base2"))
height=float(input("Enter the height"))
area = (1/2)* (base1 + base2) *height
print(" the area of a trapezoid is:",area)

#Output=>Enter the value of base1 5
Enter the value of base2 5
Enter the height 5
 the area of a trapezoid is: 25.0



#Quetion-8. Volume of a Sphere: Write a Python program to calculate the volume of a sphere given its radius.
        #Formula: Volume = (4/3) × π × radius^3

pi=3.14
radius=float(input("Enter the value of radius"))

volume= ((4/3) *pi *(radius**3))

print("the volume of a sphere is:",volume)

 #Output=>Enter the value of radius5
the volume of a sphere is: 523.3333333333334

#Question-9. Surface Area of a Cube: Write a Python program to calculate the surface area of a cube given its side length.
    #Formula: Surface Area = 6 × side length^2
side_length=float(input("Enter the Side Length"))
surface_area=6*(side_length**2)
print("The surface area of a cube is",surface_area)
#Output=>
Enter the Side Length5
The surface area of a cube is 150.0


#Question-10. Area of a Rhombus: Write a Python program to calculate the area of a rhombus given its diagonals.
    #Formula: Area = (1/2) × diagonal1 × diagonal2

diagonal1=float(input("Enter the value of diagonal 1"))
diagonal2=float(input("Enter the value of diagonal 2"))

area = (1/2)*diagonal1 * diagonal2
print("The area of a Rhombus is",area)

#Output=>
Enter the value of diagonal 15
Enter the value of diagonal 25
The area of a Rhombus is 12.5

#Question-11. Celsius to Fahrenheit Converter: Write a Python program to convert Celsius to Fahrenheit.
    #Formula: Fahrenheit = (Celsius × 9/5) + 32

Celsius=float(input("Enter the value of celsius"))
Fahrenheit = (Celsius * 9/5) + 32
print(Celsius,"Celsius is \t",Fahrenheit, "Fahrenheit")

#Output=>
Enter the value of celsius4
4.0 Celsius is 	 39.2 Fahrenheit

#Question-12. Fahrenheit to Celsius Converter: Write a Python program to convert Fahrenheit to Celsius.
    #Formula: Celsius = (Fahrenheit - 32) × 5/9

Fahrenheit=float(input("Enter the value of Fahrenheit"))
Celsius = (Fahrenheit -32)*5/9
print(Fahrenheit,"Fahrenheit is\t", Celsius, "Celsius")

#Output=>
Enter the value of Fahrenheit39.2
39.2 Fahrenheit is	 4.000000000000002 Celsius

#Question-13. Write a Python program to calculate the area and perimeter of a rectangle given its length and width.
    #Formula:
            #- Area = length * width
            #- Perimeter = 2 * (length + width)

length=int(input("Enter the Length of rectangle: "))
width=int(input("Enter the width of rectangle: "))
area = length * width
perimeter= 2 * (length + width)
print("The area of the rectangle is:",area,"and The perimeter of the rectangle is",perimeter)   

 #Output=>
Enter the Length of rectangle: 5
Enter the width of rectangle: 5
The area of the rectangle is: 25 and The perimeter of the rectangle is 20

#Question-14- Write a Python program to calculate the area and perimeter of a triangle given its base and height.
        #Formula:
                #- Area = (base * height) / 2
                #- Perimeter = base + height + √(base^2 + height^2)

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = (base * height) / 2
perimeter=base + height +((base**2 + height**2)**0.5)#√25 =root of 25 so (25)^1/2 
print("The area of the triangle is:", area,"and The perimeter of the triangle is",perimeter)

#Output=>
Enter the base of the triangle: 5
Enter the height of the triangle: 5
The area of the triangle is: 12.5 and The perimeter of the triangle is 17.071067811865476

#Question-15.Write a Python program to calculate the area of a circle.
        #Formula: Area = π * r^2

pi=float(3.14)
r=float(input("Enter the radious of circle:"))
Area = pi *(r**2)
print("The area of a circle is:",Area)

#Output=>
Enter the radious of circle:5
The area of a circle is: 78.5

#Question-16. Write a Python program to calculate the circumference of a circle.
        #Formula: Circumference = 2 * π * r

pi=float(3.14)
r=float(input("Enter the radious of circle:"))
Circumference = 2 * pi * r
print("The Circumference of circle is:",Circumference)

#Output=>
Enter the radious of circle:5
The Circumference of circle is: 31.400000000000002

#Question-17. Write a Python program to calculate the volume of a cylinder.
        #Formula: Volume = π * r^2 * h

pi=float(3.14)
r=float(input("Enter the radious of cylinder:"))#3
h=float(input("Enter the height of cylinder:"))#5

volume = pi * (r**2) *h
print("The volume of cylinder is:",volume)#141.3

#Output=>
Enter the radious of cylinder:3
Enter the height of cylinder:5
The volume of cylinder is: 141.3
'''
#Question-18. Write a Python program to calculate the surface area of a sphere.
        #Formula: Surface Area = 4 * π * r^2

pi=float(3.14)
r=float(input("Enter the radious of cylinder:"))#3
surface_area= 4* pi * (r**2)
print("The Surface Area of a sphere is:",surface_area)#113.04

#Output=>
Enter the radious of cylinder:3
The Surface Area of a sphere is: 113.04s
