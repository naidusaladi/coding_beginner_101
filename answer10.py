arr = list(map(int,input("Enter the number separated by space:").split()))
word = ""
lenof = len(arr)
for i in range(lenof):
    word = " " + str(arr[i]) + word
print(word.strip())

# i take help from chatgpt and sloved it