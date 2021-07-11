n=int(input("enter the number......"))
i=2
while i<n:
	if n%i==0:
		print(i,"it is not prime number")
		break
	i=i+1
else:
	print(i," it is prime number")