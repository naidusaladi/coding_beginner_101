user = input("enter number: ")
#len_user = len(user) actually i don't need this also
high_num = 0
"""if len_user == 1:
    print(user)         i write this because it stops when the input is single charater
    break """
for i in user :
    if (int(i) > high_num):
        high_num = int(i)
print(high_num)


