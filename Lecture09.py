# Strings are immutable
a = "!!!Unknown!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.strip())
print(a.rstrip("!"))
print(a.replace("Unknown","John"))
print(a.split(" "))

blogHeading = "introduction to js"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))
print(str1.endswith("!!!"))
print(str1.endswith("to",4,10))

str2 = "He's name is Dan. He is an honest man."
print(str2.find("is")) # If the word is not found it returns -1
print(str2.index("Dan"))

str3 = "WelcomeToTheConsole"
print(str3.isalnum())

str4 = "Welcome00"
print(str4.isalpha())
print(str4.islower())
print(str4.isprintable())

str5 = "             "     #using Spacebar
print(str5.isspace())

str6 = "World Health Organization"
print(str6.istitle())

str7 = "To kill a Mocking bird"
print(str7.istitle())

str8 = "Python is a Interpreted Language"
print(str8.startswith("Python"))
print(str8.swapcase())

str9 = "His name is Dan. Dan is an honest man."
print(str9.title())





