# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=[]
for i in range(n):
    l.append(input())
for i in l:
    print(i[0:len(i)+1:2],i[1:len(i)+1:2])
