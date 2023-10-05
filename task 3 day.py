a=[2,5,9,8,7,7,7,6,7,4]
b=[]
# for unique value in lists
for i in a:
    if i not in b:
        b.append(i)
print("the given list:",a)
print("unique values in given numbers:",b)

# for counting the number of 7 exsist
print("the number of 7 exists:", a.count(7))

# for finding the second largest number in given lists
a.sort()
print("the second largest number in given list:", a[-2])
