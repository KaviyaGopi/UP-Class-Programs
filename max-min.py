k = int(input("enter the K value: "))
total_entry = int(input("How many numbers you want in your tuple: "))
ourList = []
for i in range(total_entry):
    ourList.append(int(input(f"Enter the {i+1}th Entry: ")))
ourList.sort()
newList = []
for i in range(k):
    newList.append(ourList[i])
    newList.append(ourList[-1-i])
newList.sort()
ourTuple = tuple(newList)
print(ourTuple)