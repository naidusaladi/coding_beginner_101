a = input("enter string: ")
count = len(a)
last_lettter = count - 1
if (a[0] == "") and (a[last_lettter] == "") :
    print("you have not entered any word")
elif a[0] == a[last_lettter]:
    print("True")
else:
    print("False")