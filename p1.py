#lambda function

s=lambda x:x*x*x*x
print (s(2))

li =[5,10,15,22,14,56,14]
finallist =list(map(lambda x:x*2,li))
print (finallist)


firstlist =list(filter(lambda x:(x%2 !=0),li))
print(firstlist)


from functools import reduce
sum =reduce((lambda x,y :x+y),li)
print(sum)
