num=int(input("enter any number"))
var=num
while sum!=1 and sum!=4:
	sum=0
	while var!=0:
		a=int(var%10)
		sum=sum+a*a
		var=var/10
	var=sum
if sum==1:
	print(num,"is Happy Number")
else:
	print(num,"is Unhappy Number")
