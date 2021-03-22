def merge(a,l,m,r):
	n1=m-l+1
	n2=r-m
	
	l1=[0]*n1
	l2=[0]*n2

	for i in range(0,n1):
		l1[i]=a[l+i]
	for j in range(0,n2):
		l2[j]=a[m+1+j]
	
	i=0
	j=0
	k=l
	while(i<n1 and j<n2):
		if(l1[i]<l2[j]):
			a[k]=l1[i]
			i=i+1
			c=c+1
		else:
			a[k]=l2[j]
			j=j+1
			c=c+1
		k=k+1
	while(i<n1):
		a[k]=l1[i]
		i+=1
		k+=1
	while(j<n2):
		a[k]=l2[j]
		j+=1
		k+=1
	print(c)
def mergesort(a,l,r):
	if(l<r):
		m=(l+(r-1))//2
		mergesort(a,l,m)
		mergesort(a,m+1,r)
		merge(a,l,m,r)
n=int(input())
a=list(map(int,input().split(" ")))
mergesort(a,0,n-1)
print(a)
			