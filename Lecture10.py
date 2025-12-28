# if-else statement
a = int(input("Enter your age:"))
print("Your age is:",a)

if(a>1):
    print("You can drive.")
else:
    print("You cannot drive.")
# elif statement
num = int(input("Enter the value of num:"))
if(num < 0):
    print("Number is negative")
elif(num == 0):
    print("Number is Zero...")
else:
    print("Number is positive")

b = float(input("Enter your marks:"))
print("Your marks is:",b)
if(b < 0 or b > 100):
    print("Invalid Marks!!!")
elif(b <= 20):
    print("E Grade...")
elif(b <= 40):
    print("D Grade...")
elif(b <= 60):
    print("C Grade...")
elif(b <= 80):
    print("B Grade...")
else:
    print("A Grade...")

# nested-if statement
c = 10
if(c < 0):
    print("c is negative")
elif(c > 0):
    if(c <= 10):
        print("c is between 1-10")
    elif(c > 10 and c <= 20):
        print("c is between 11-20")
    else:
        print("c is greater than 20")
else:
    print("c is equal to zero")