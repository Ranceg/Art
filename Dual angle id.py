# Doubles the trig functions of a trigon
while True:
    o = int(raw_input("Opposite?: "))
    a = int(raw_input("Adjacent?: "))
    h = int(raw_input("Hypotenuse?: "))
    d = h
    sin = o
    cos =a
    tan = sin,'/',cos
    sin2t = 2*sin*cos
    cos2t = (cos*cos) - (sin*sin)
    tan2t = sin2t/cos2t
    tan = sin2t,'/',cos2t
    print '----------------------'
    print 'Cos 2 theta is ',cos2t,'/',d*d
    print '----------------------'
    #print 'Tan 2 theta is ',tan2t
    print 'Sin 2 theta is ',sin2t,'/',d*d
    print '----------------------'
    '''print 'Sin is ', sin,'/',d
    print 'Cos is ',cos,'/',d'''
    print 'Tan is ', tan

