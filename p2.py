
def fact(a):

	num =a
	factorial =1
	if num < 0:
		print("the factorial is not posiable")
	elif num == 0:
		print("the factorial of 0 is 1")
	else :
		for i in range(1,num+1):
			factorial = factorial*i
		print(factorial)
#fact()

def revers(a):
	num= a
	rev =0
	while(num>0):
		div =num%10
		rev =rev*10+div
		num =num//10
	print("the revers value is"+ str(rev))

#revers(15826)

def result():
	while(num>0):
		div =num%10
		rev =rev*10+div
		num =num//10	
def palindrome(a):
	num= a
	temp =num
	rev =0
	
	result()
	if temp ==rev:
		print("the number is palindrome")
	else :
		print("the num is not palindrome")
palindrome(122)

def fibonacci():
	num =10
	a=0
	b=1
	print(a)
	if num < 0 :
		print("incorret input")
	elif num==0 :
		print(a)
	elif num==1 :
		print(b)
	else :
		for i in range(2,num+1):
			c = a+b 
			a = b
			b = c 
			print(a)
		#print(b) 

#fibonacci()