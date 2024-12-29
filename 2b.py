def display_menu():
    print("Welcome to number conversion")
    print("1. Binary to Decimal")
    print("2.Octal to hexadecmial")
    print("3. Exit")

def bin_to_dec():
    bin_num=input("Enter the binary number to be converted")
    try:
        dec_num = int(bin_num, 2)
        print("Decimal equivalent",dec_num)
    except ValueError:
        print("Error")

def oct_to_hexa():
    oct_num=input("Enter the octal number to be converted")
    try:
        dec_num=int(oct_num, 8)
        hex_num=hex(dec_num)
        print("The hexadecimal equavilent",hex_num)
    except ValueError:
        print("Error") 

while True:
    display_menu()
    choice=input("Enter your choice")
    if choice=='1':
        bin_to_dec()
    elif choice=='2':
        oct_to_hexa()
    elif choice=='3':
        break
    else:
        print("Enter a valid input ")
