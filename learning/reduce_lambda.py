#!/usr/bin/python
##The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value.

##If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:

##   At first the first two elements of seq will be applied to func, i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
##   In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
##  The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
##  Continue like this until just one element is left and return this element as the result of reduce()


reduce(lambda x,y: x+y , [47,11,42,13])

##EG 1 finding max
f = lambda a,b : a if (a>b) else b
reduce(f,[47,11,42,102,13])
##EG 2 finding sum from 1 to 101
reduce(lambda x,y: x+y ,range(1,101)