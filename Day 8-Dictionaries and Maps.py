import sys
n=int(input())
phoneBook={}
for i in range(n):
    x,y=map(str,input().split(' '))
    phoneBook[x]=y
lines = sys.stdin.readlines()
for i in lines:
    i=i.strip()
    if i in phoneBook:
        print("%s=%s"%(i,phoneBook[i]))
    else:
        print("Not found")
