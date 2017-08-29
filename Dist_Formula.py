import math as m

def r(x1, y1, x2, y2):
    #All i need is the center coordinates and a pointon the circle
    x = x2 - x1
    y = y2 - y1
    r = (x*x) + (y*y)
    return 'Radius = ',m.sqrt(r), ' or sqrt('+str(r)+')'

def d(x1, y1, x2, y2):
    #All i need is the endpoint coordinates...
    x = (x1 + x2)/2
    y = (y1 + y2)/2
    mid = x,y
    print 'Center is at', mid
    return r(x1,y2,x,y)

'''print 'x1 : ' , x1
print 'y1 : ' , y1
print 'x2 : ' , x2
print 'y2 : ' , y2
'''
