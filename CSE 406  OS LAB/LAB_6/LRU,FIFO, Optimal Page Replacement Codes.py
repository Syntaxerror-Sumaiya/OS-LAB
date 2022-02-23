#LRU Page Replacement


a=[]
sum=0
f= int (input("Enter No Of Frames:  "))
check= input("Do You Want To Use User Input [y/n]: ")
if check=='y':
    a=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
    print("Inputs are: ", a)
else:
    n= int (input("Enter no of String : "))
    print("Enter the string: ")
    for i in range(n):
      t= int (input())
      a.append(t)
n=len(a)
m=[]
c=[]
t=[]
total=0
idx=0
for i in range(f):
    m.append(-1)
    t.append(0)

print('\nOutput wil be: ')
for i in range(n):
    test=0
    for p in range(f):
        c.append(m[p])

    for j in range(f):
        if a[i]==m[j]:
            test=1
            total+=1
            t[j]=total
            break
    if test==0:
        idx=t.index(min(t))
        m[idx]= a[i]
        total+=1
        t[idx]=total
        sum+=1


    if c==m:
        for q in range(f):
            print('-',end=' ')
    else:
        for q in range(f):
            if m[q]==-1:
                print("-",end=' ')
            else:
                print(m[q],end=' ')
    c.clear()
    print()

print("Page Fault: ",sum)






#FIFO Page Replacement

a=[]
sum=0
f= int (input("Enter No Of Frames: "))
check= input("Do You Want To Use User Input [y/n]: ")
if check=='y':
    a=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
    print("Inputs are: ",a)
else:
    n= int (input("Enter no of String : "))
    print("Enter the string: ")
    for i in range(n):
      t= int (input())
      a.append(t)
n=len(a)
print(n)
m=[]
c=[]
for i in range(f):
    m.append(-1)
count=0
print('\n Output wil be: ')
for i in range(n):
    test=0
    p=0
    for p in range(f):
        c.append(m[p])

    if count>=f:
        count=0
    for j in range(f):
        if a[i]==m[j]:
            test=1
            break
    if test==0:
        m[count]= a[i]
        count+=1
        sum+=1


    if c==m:
        for q in range(f):
            print('-',end=' ')
    else:
        for q in range(f):
            if m[q]==-1:
                print("-",end=' ')
            else:
                print(m[q],end=' ')
    c.clear()
    print()
print("Page Fault: ",sum)






#Optimal Page Replacement Algorithm

a=[]
sum=0
f= int (input("Enter No Of Frames:  "))
check= input("Do You Want To Use User Input [y/n]: ")
if check=='y':
    a=[3,2,3,1,4,1,4,2,6,1,2,4,1,5,3,6,1,2,3,1]
    print("Inputs are: ", a)
else:
    n= int (input("Enter no of String : "))
    print("Enter the string: ")
    for i in range(n):
      t= int (input())
      a.append(t)
n=len(a)
m=[]
c=[]
l=[]
for i in range(f):
    m.append(-1)

print('\nOutput wil be: ')
for i in range(n):
    test=0
    for p in range(f):
        c.append(m[p])
    if i<f:
        m[i]=a[i]
        sum+=1
        a[i]=-99
    else:
        for j in range(f):
            if a[i]==m[j]:
                test=1
                a[i]=-99
                break
        if test==0:
            for s in range(f):
                if(m[s] in a):
                    l.append(a.index(m[s]))
                else:
                    l.append(999)
            idx=l.index(max(l))
            m[idx]=a[i]
            sum+=1
            a[i]=-99


    if c==m:
        for q in range(f):
            print('-',end=' ')
    else:
        for q in range(f):
            if m[q]==-1:
                print("-",end=' ')
            else:
                print(m[q],end=' ')
    c.clear()
    l.clear()
    print()

print("Page Fault: ",sum)