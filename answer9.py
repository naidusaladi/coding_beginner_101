"""num = input()
len_num = (len(num)-1)

for i in num:
    diff_num = int(int(i) - diff_num)
print(diff_num)                             it takes me to write code 50 mins but worth it!

for i in range(1,len_num):
    if i == "":
        print(num[0])
    else:"""
a = input("Enter the number: ")
len_a = len(a)
first_num = int(a[0])
#condition = 0
if len_a == 1:
    print(a)
else:
    for i in range(1,len_a ):
        first_num = first_num - int(a[i])
    print(first_num)
        