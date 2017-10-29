#Find A(amplitude)
#Made with python3
#Designed to assist me with quickly graphing in Pre-Calc class
import math
while 1 == 1:
    A = float(input("Enter Amplutude : "))
    A = abs(A)

#Find B (Horizontal Stretch/Shrink)
    B = float(input(" Enter B : "))

#Find C (Horizontal Shift L/R)
    C = float(input(" Enter C : "))

#Find D (Start on y axis)
    D = float(input(" Enter D : "))
    pi = round(math.pi)

#find period
    if B == 2:
        period = pi
    else:
        period = (2*pi)/B

    print("Period = ",period)

#find Increment(Inc)
    Inc = period/4
    print("Increment = ",Inc)

#find phase shift(PS)
    PS = (C)/B
    X1 = PS
    X2 = X1 + Inc
    X3 = X2 + Inc
    X4 = X3 + Inc
    X5 = X4 + Inc
    print("Phase Shift = ", PS)
    
    input(" Ready for key points?")
    
   
    print("X1 = ", X1)
    input("...")
    print("X2 = ", X2)
    input("...")
    print("X3 = ", X3)
    input("...")
    print("X4 = ", X4)
    input("...")
    print("X5 = ", X5)


