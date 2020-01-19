user={'admin':True,'active':True,'name':'Kevin'};
print("admin :", user['name']);
if(user['active']):
    print("active :", user['name']);
if(user['active'] and user['admin']):
    print("active - admin :", user['name']);
if(not user['active'] and not user['admin']):
    print( user['name']);

usersList=[
    {'admin':True,'active':True,'name':'Kevin'},
    {'admin':True,'active':False,'name':'Elizabeth'},
    {'admin':False,'active':True,'name':'josh'},
    {'admin':False,'active':False,'name':'kim'}
]

for user in usersList:
    if(user['active'] and user['admin']):
        print("active - admin :", user['name']);
    elif(user['active']):
        print("active :", user['name']);
    elif(user['admin']):
        print("admin :", user['name']);
    else:
        print( user['name']);