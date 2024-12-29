val=int(input("Enter the string"))
str_val=str(val)

if str_val==str_val[::-1]:
    print("palindrome")
else:
    print("Not palindrome")
for i in range(10):
    if str_val.count(str(i)) >0:
        print(str_val,"appears",str_val.count(str(i)),"times")