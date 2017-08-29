import math
from mpmath import *
deg = math.radians
sin = math.sin
#asin = math.asin
#def findangle():
    
def SSA():
    B = float(raw_input('Enter angle B : '))
    c = float(raw_input('Enter side c : '))
    b = float(raw_input('Enter side b : '))
    bee = B
    B = deg(B)
#find an angle of side we have
    C = float(c*sin(B))/b
    print 'Plug this ',C, ' in calc like : sin^-1(',C,') [Thats your angle]'
    angle = float(raw_input('Give me your angle : '))
    ma = 180 - (angle+bee)
    print 'Missing angle is', ma
    #find a
    print 'this is the point where things stop working'
    #do MA*b
    idk = sin(bee)
    ma = deg(ma)
    man = sin(ma)*b
    a = round(man / idk, 2)
    print 'Side a is', a
    one = b*math.degrees(sin(A))
    two = one / a
    print two
    three = float(asin(deg(two)))
    print three
    '''Aswer is 15.52  where B = 31 b = 8 and c = 13''' 
#    a*sin(x)
    print rad
def AREA(): #working!!!
    A = float(raw_input('Enter angle A : '))
    a = float(raw_input('Enter side c : '))
    b = float(raw_input('Enter side b : '))
    A = deg(A)
    A = .5*a*b*sin(A)
    print 'Area = ',round(A,2)
def NOT(): #working!!!
    #Number of triangles
    A = float(raw_input('Enter angle A : '))
    a = float(raw_input('Enter side a : '))
    b = float(raw_input('Enter side b : '))
    A = deg(A)
    h = b*sin(A)
    print h
    if a < h:
        print '0 solution'
    elif a == h or a > b:
        print '1 solution'
    elif b > a > h:
        print '2 solution'
  
