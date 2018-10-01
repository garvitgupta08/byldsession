#name- garvit gupta
#roll no. 2018141
#section- A
#group- 5
def decimalrep(n):
	'''	if 0<=n<=9:
		decrep=n
	elif n==10:
		decrep="a"
	elif n==11:
		decrep="b"
	elif n==12:
		decrep="c"
	elif n==13:
		decrep="d"
	elif n==14:
		decrep="e"
	elif n==15:
		decrep="f"
	
		
		
	else:'''
	d=""
	while int(n/16)>0:
		x=n%16
		if int(n/16)==0:
			if 0<=x<=9:
				x=x
			elif x==10:
				x="a"
			elif x==11:
				x="b"
				break
			elif x==12:
				x="c"
				break
			elif x==13:
				x="d"
				break
			elif x==14:
				x="e"
				break
			elif x==16:
				x="f"
				break
		elif 0<=x<=9:
			x=x
		elif x==10:
			x="a"
		elif x==11:
			x="b"
		elif x==12:
			x="c"
		elif x==13:
			x="d"
		elif x==14:
			x="e"
		elif x==15:
			x="f"
		
				
		x=str(x)
			
			
			
		d=x+d
		
		n=int(n/16)
			
	x=str(x)
	d=x+d
	decrep=d
	return decrep
s=input("enter in hexadecimal format: ")
count=0
for i in s:
	a="0123456789abcdef"
	b=a.index(i)
	c=s.index(i)
	power=len(s)-(c+1)
	count+=b*16**power
a=count
if a%5==0:
	d="the number is divisible by 5"

	c=int(a/5)
	
	
	
	b=decimalrep(c)
	
else:
	d="the number is not divisible by 5"
	b="no display of quotient"
print(d)
print("the quotient is:",b)


	