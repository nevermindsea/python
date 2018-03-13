#!/usr/bin/python

def fahrenheit(T):
	return ((float(9)/5)*T+32)

def celcius(T):	
	return ((float(5)/9)*(T-32))
	
	
celcius(33.8)
fahrenheit(1)


temp = [36.5,37,37.5,39]

F = list(map(fahrenheit,temp))
C = list(map(celcius,F))

## Lambda
Celcius =  [36.5,37,37.5,39]
Fahrenheit = list(map(lambda x: (float(9)/5)*x+32,Celcius))

C = list(ap(lambda x: (float(5)/9)*(x-32),Fahrenheit))


## 2 lists
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
list(map(lambda x,y,z: x+y+z,a,b,c))



