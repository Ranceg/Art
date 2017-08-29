import sympy
def sin():
    print("Unit Circle")
    print("Angle             Sine Value")
    print("-----------------------------------")
    
    for i in range(0, 375, 15):
        print( i, "                ",sympy.sin(sympy.Rational(i, 180) * sympy.pi))
def cos():
    print("Unit Circle")
    print("Angle             Cosine Value")
    print("---------------------------------------")
    
    for i in range(0, 375, 15):
        print( i, "                  ",sympy.cos(sympy.Rational(i, 180) * sympy.pi))
def unit():
    print("Unit Circle")
    print("Angle             Coordinate")
    print("---------------------------------------")

    for i in range(0, 375, 15):
        print( i, "                ",'(',sympy.cos(sympy.Rational(i, 180) * sympy.pi),',', sympy.sin(sympy.Rational(i, 180) * sympy.pi),')')
def search(degree,fun):
    fun = str(fun)
    #sym = sympy.function
    if fun == 'cos':
        cos = "The ",fun, "of ", degree , "degrees is : ",sympy.cos(sympy.Rational(degree, 180) * sympy.pi)
        print (cos)
    elif fun == 'sin':
        sin = "The ",fun, "of ", degree , "degrees is : ",sympy.sin(sympy.Rational(degree, 180) * sympy.pi)
        print (sin)
    else:
        print("error")
        print(degree)
        print(str(fun))

    
    
    
