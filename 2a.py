def fibnoacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibnoacci(n-1)+fibnoacci(n-2)
try:
    n=int(input("Enter the number "))
    if n<0:
        print("Enter a valid no (N>0)")
    else:
        result=fibnoacci(n)
        print(f"fibnoacci({n})={result}")

except ValueError:
    print("Enter a valid number (N>0).")  