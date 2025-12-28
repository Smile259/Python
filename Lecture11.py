# Create a python program capable of greeting you with Good Morning,Good Afternoon and Good Evening.Your program should use time module to get the current hour.
import time
timestamp = time.strftime('%H:%M:%S')
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

hour = int(time.strftime('%H'))
print("Current Hour:",hour)
if(hour < 12):
    print("Good Morning!!!")
elif(hour == 12):
    print("Good Afternoon!!!")
else:
    print("Good Evening!!!")