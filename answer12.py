arr = list(input("enter the strings separated by space: ").split())
len_arr = len(arr)
if len_arr == 0:
    print("None")
else:
    high = ""
    start_c = arr[0]
    for i in arr:
        if (len(start_c) < len(i)):
            start_c = i
    print(start_c)
            
    