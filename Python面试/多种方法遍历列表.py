list1 = [1, 1, 2, 3, 4, 5]
# 1
for i in range(len(list1)):
    print(i, list1[i])
for i,val in enumerate(list1):
    print(i,val)
for i in list1:
    print(list1.index(i),i)
