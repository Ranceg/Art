 #find nth term
x = 0
z = 1
times = input("Loop how many times?: ")
while(x <= times - 1):
    first = input("Enter first digit in sequence: ")
    n = input("Enter the number you seek in the sequence: ")
    step = input("Pattern stepping?: ")
    if n == 0:
        test = input("What number do you want to test for?: ")
        seq = (test - first +1 )/step
        
        if seq is int:
            print "Number in sequence!"
            print seq
            
        else:
            print "Not in sequence!"
    
    
    
    term = first + (n -1)*step
    '''pall = raw_input('Print first 100 terms?[Y/N]')
    pall = pall.lower()
    if pall == 'Y':
    
        for i in range(100):
            n = 1
            print term,','
            n +=1
      '''      
    print term
    x += 1
