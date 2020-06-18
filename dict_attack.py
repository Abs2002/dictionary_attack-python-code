import hashlib

hash=input(">>>")

f=open("password_list.txt", "r")
a=f.read()
f.close()
b=a.split()
crypt=hashlib.md5()

found=0
i=0
while i<len(b):
    crypt.update(bytes(b[i],"utf-8"))
    l=crypt.hexdigest()
    if l==hash:
        print("your password is : ", b[i])
        found+=1
        break
    i+=1

if found==0:
    print("can't find the password")


