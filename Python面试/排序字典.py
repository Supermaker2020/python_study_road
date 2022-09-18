dict1={'1':1,'2':2,'3':3}
list1=dict1.items()
print(list1)
list2=sorted(list1,key=lambda i :i[0],reverse=True)
print(list2)
dict2=dict(list2)
print(dict2)