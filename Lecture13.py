# For Loops
# Iterating over a string
name = "Abhishek"
for i in name:
    print(i)
    if(i == "b"):
        print("This is a constant")

# Iterating over a string
colors = ["Red","Green","Blue","Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

#Range() function
for k in range(1,10000):
    print(k+1)

for x in range(1,12,3):
    print(x)