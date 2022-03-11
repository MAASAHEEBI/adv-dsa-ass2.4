#4) Implement insertion Sort
a=[]
n=int(input("enter size of the list:"))
for i in range(n):
    val=int(input("enter number:"))
    a.append(val)
    
for i in range(1,n):
    t=a[i]
    j=i-1
    while j>=0 and t<a[j]:
        a[j+1]=a[j]
        j=j-1
        a[j+1]=t
print("sorted list is:")
print(a)
