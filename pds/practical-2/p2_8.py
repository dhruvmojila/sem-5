a = ['d','h','r','u','v']
print("join method:", ''.join(a))
b = ','.join(a)
print("split method:", b.split(','))
d = {
'neharika':{'birthday':'Jun 1'},
'soham':{'birthday':'june 30'},
'preyas':{'birthday':'July 7'},
'divyam':{'birthday':'may 5'}
}
name = input("enter name:")
print("birthday:", d[name])
