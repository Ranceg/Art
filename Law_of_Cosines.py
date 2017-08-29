#SSS (Solves a triangle with three known sides using Law Of Cosines
import math as m
s = int(input("How many questions?: "))
num = 0

'''def repeat(times, f):
    for i in range(times): f()
def main():    '''
while num < s:
    choice = raw_input("SSS or SAS? :")
    choice = choice.lower()
    if choice == "sss": 
    #sides
        wangle = raw_input("Which angle are you looking for? [A,B,C]: ")
        if wangle == "A":        
            a = float(input("Enter side A: "))
            b = float(input("Enter side B: "))
            c = float(input("Enter side C: "))
            a2 = a*a
            b2 = b*b
            c2 = c*c
            aangle = (b2+c2-a2)/(2*b*c)
            A = round(m.degrees(m.acos(aangle)),2)
            print("Angle A is ", A, "degrees!")
        elif wangle == "B":       
            a = float(input("Enter side A: "))
            b = float(input("Enter side B: "))
            c = float(input("Enter side C: "))
            c2 = c*c
            a2 = a*a
            b2 = b*b
            bangle = (a2+c2-b2)/(2*a*c)
            B = round(m.degrees(m.acos(bangle)),2)
            print("Angle B is ", B, "degrees!")
        elif wangle == "C":        
            a = float(input("Enter side A: "))
            b = float(input("Enter side B: "))
            c = float(input("Enter side C: "))
            a2 = a*a
            b2 = b*b
            c2 = c*c
            cangle = (a2+b2-c2)/(2*a*b)
            C = round(m.degrees(m.acos(cangle)),2)
            print("Angle C is ", C, "degrees!")
        '''if aangle + bangle + cangle == 180:
            print("Sum of angles = 180")
        else:
        print("Error, Sum of angles(",aangle,bangle,cangle,") doesn't equal 180!")'''
       #-------------------------------------------SAS------------------------------------------------- 
    elif choice == "sas":   
        #angles
        wside = raw_input("Which side are you looking for? [A,B,C]: ")
        wside = wside.lower()
        if wside == "a":
            b = float(input("Enter side B: "))
            c = float(input("Enter side C: "))
            A = float(input("Enter angle A: "))
            b2 = b*b
            c2 = c*c
            arad = m.radians(A)
            a = b2+c2 - 2*(b*c)*m.cos(arad)
            aside = round(m.sqrt(a),2)
            print("Side A is " ,aside," Units")
            print(a)
        elif wside == "b":
            # B test : A = 14, B= 19 , C= 8 Should get -.45
            a = float(input("Enter side A: "))
            c = float(input("Enter side C: "))
            B = float(input("Enter angle B: "))
            a2 = a*a
            b2 = b*b
            c2 = c*c
            brad = m.radians(B)
            b = a2+c2 - 2*(a*c)*m.cos(brad) 
            bside = round(m.sqrt(b),2)
            print("Side B is " ,bside," Units")
            print(b)
        elif wside == "c":
            a = float(input("Enter side A: "))
            b = float(input("Enter side B: "))
            C = float(input("Enter angle C: "))
            a2 = a*a
            b2 = b*b        
            crad = m.radians(C)
            c = a2+b2 - 2*(b*a)*m.cos(crad)
            cside = round(m.sqrt(c),2)
            print("Side C is " ,cside," Units")
            print(c)
    num += 1

#print(aside)
#A = m.acos(A)
