str1=input("Enter a value")
words=str1.split()
print("Number of words entered",len(words))
digits=[]
u_letters=[]
l_letters=[]
spl_char=[]
for i in str1:
    if i.isdecimal():
        digits.append(i)
    elif i.isupper():
        u_letters.append(i)
    elif i.islower():
        l_letters.append(i)
    else:
        spl_char.append(i)

    print("Number of digits:",len(words),digits)
    print("Number of uppercase letter",len(words),u_letters)
    print("Number of lowercase letter",len(words),l_letters)
    print("Number of special characters",len(w  ords),spl_char)