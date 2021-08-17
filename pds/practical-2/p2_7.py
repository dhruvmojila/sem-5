str=input("enter string: ")
print('String : ',str)
dict = {}
for i in str:
    keys = dict.keys()
    if i in keys:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)
