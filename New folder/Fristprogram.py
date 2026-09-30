#Double every numbner
nums=[1,2,3,4]
x=list(map(lambda n:n*2,nums))
print(x)

nums=[1,2,-3,6,-8]
l=list(filter(lambda n:n>=0,nums))
print(l)


w=lambda n:n**3
print(w(7))
print(w(3))
print(w(7))


words=["python","lambda","map"]
m=list(map(lambda n:n.upper(),words))
print(m)

nums=[1,2,3,4,5,6,7,8,9,10,11,12,1,3,14,15,16,17,18,19,20]
i=list(filter(lambda n:n%2!=0,nums))
print(i)


###sort by letter
names=["Amit",'Neha',"Ravi","Sra"]
names.sort(key=lambda n:n[-1])
print(names)

###Clean the price
raw=["$100","$250","$99"]
c=list(filter(lambda d: d>100,map(lambda n: int(n.replace("$","")),raw)))
print(c)




from functools import reduce
##Longest Word with reduce
word=["hi","python","lambda","ok"]
d=reduce(lambda a,b : a if len(a) >=len(b) else b,word)
print(d)

print("Hello")