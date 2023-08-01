def simple_interest(p,r,n):
	print("Enter the principal:",p)
	print("Enter the rate of interest:",r)
	print("Enter the number of year:",n)

	si = (p*r*n)/100
	print("\nInterest of Amount =",si)
	pay = p+si
	print("\nPay Amount =",pay)
simple_interest(5000,8,2)