a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))
if a > b and a > c :
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)