# Match case statements

x = int(input("Enter the value of x: "))
print("The value of x is ",x)

match x:                   # x is the variable to match
    case 0:                
        print("x is zero") 
    case 4:                
        print("x is four")
    case _:               # Default case
        print(x)


y = int(input("Enter the value of y:"))
# y is the variable to match
match y:
    # if y is 0
    case 0:
        print("y is zero...")
    # case with if-condition
    case 4: print("case is 4")

    case _ if y!=90:
        print(y,"is not 90")
    case _ if y!=80:
        print(y,"is not 80")
    case _:
        print(y)