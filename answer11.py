arr = list(input("enter the strings separated by space: ").split())
len_arr = len(arr)
if len_arr == 0:
    print("None")
else:
    for i in arr:
        if i[0] == "b":
            print(i)