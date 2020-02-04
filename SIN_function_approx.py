# -----------------------------------------------------------#
# (C) 2020 Matthew Cann
# Released under MIT Public License (MIT)
# email mcann@uwaterloo.ca
# -----------------------------------------------------------

# Part A 
#IMPORTS........................................................................
import math
import time

# Title and Coloumn headings...................................................
print("ASSIGNMENT 2: SUMMING SERIES \n")
print ("A: TERMS OF THE SIN(X) SERIES FOR X=2"U"\N{GREEK SMALL LETTER PI}","\n")
print ("Count","        Term","                Total")

# Calculations.................................................................
xx = 2*math.pi             # [rads] Value of x
xsq = xx**2                # Value of xx^2 in nominator
SMALL = 10**-20            # Small number for the loops limit
count = 0                  # Number of terms added so far
total = 0.0                # Total of terms so far
term = Product = xx        # First term is xx
while abs(term) > SMALL:
    total += term          # Updates total
    count += 1             # Updates count
    print ("%4.d   %20.16f   %20.16f" %(count,term,total))
    Product *= -xsq / ((2.0 * count) * (2.0 * count + 1))   #next term in the series
    term = Product                                      #Product becomes term
print ("\n Final value of series is", total,"\n")
print ('Programmed by 'u'\u2606' 'Matt Cann'u'\u2606''\nDate: ',time.ctime(),' \nEnd of processing''\n')
print ('\n'  )


#Part B........................................................................

#
# Title and Column headings....................................................
print ("B: TABULATING SIN EVERY 60° USING FLOATS\n")
print ('Angle','               sin(a)','                       Difference',\
' # of ','  Largest')
print (U"[\N{DEGREE SIGN}" ']','        From math','             From Series'\
,'               terms','   term')

# Calculations.................................................................
angle = 1                        # [degrees] First angle in degrees
while angle < 2400:
    xx = angle * (math.pi) / 180 # [rads] conversion to radians
    value = math.sin(xx)         # Imported value of sin(xx) to compare too
    xsq = xx**2                  # Value of x^2
    count = 0                    # Number of terms added so far
    total = 0.0                  # Total of terms so far
    term = Product = xx          # First term is xx
    maxSoFar = 0                 # Starting max is 0
    
# Inner Loop from Part A with slight variations ...............................
    while abs(term) > 10**-20:
        maxSoFar =  max(maxSoFar, abs(term))
        total += term
        count += 1
        #print "%4.d %20.16f %20.16f" %(count,term, total)
        Product *= -xsq / ((2.0 * count) * (2.0 * count + 1))
        term = Product
        difference = total - value # Difference between series and imported num
    print ("%4.0f  %20.16f %20.16f    %10.3e %3.0i  %10.3g" \
    %(angle, value, total, difference, count, maxSoFar))
    angle += 60         # [degrees] Increase angle by 60 degrees
print ('\n Programmed by 'u'\u2606' 'Matt Cann'u'\u2606''\nDate: ',time.ctime(),' \nEnd of processing''\n')
print ('\n')


#Part C........................................................................

#
#Title and Column headings.....................................................
print ('C. TABULATING SIN EVERY 60° USING INTS \n')
print ('Angle','               sin(a)','                       Difference',\
' # of ','  Largest')
print (U"[\N{DEGREE SIGN}" ']','        From math','             From Series'\
,'               terms','   term')

# Calculations of Part B.......................................................
M_ = 10**30                        # Large number to multiple term by
angle = 1                          # [degrees] Starting angle in degrees
while angle < 2400:
    xx = angle * (math.pi) / 180   # [rads] Conversions to radians
    xsq = xx**2                    # Value of x^2
    count = 0                      # Number of terms added so far
    total = 0.0                    # Total so far
    term = Product = xx            # First term is xx
    value = math.sin(xx)           # Imported value of sin(xx) to compare too
    maxSoFar = 0                   # Starting max is 0
    
    while abs(term) > SMALL:
        maxSoFar =  max(maxSoFar, abs(term))
        term *= M_                 # Multiple term to get large number
        total += term
        count += 1
        #print "%4.d %20.16f %20.16f" %(count,term, total)
        Product = (Product * -xsq) / ((2 * count) * (2 * count + 1))
        term = Product
    
    total /= M_
    maxSoFar /= M_
    difference = total - value
    print ("%4.0d  %20.16f %20.16f    %10.3e %3.0d  %10.3g" \
    %(angle, value, total, difference, count, maxSoFar))
    angle += 60
print ('\nProgrammed by 'u'\u2606' 'Matt Cann'u'\u2606''\nDate: ',time.ctime(),' \nEnd of processing''\n')  
print ('\n')

#Part D........................................................................

#
#Title and Column headings.....................................................
print ("D. TABULATING SIN EVERY 60° MOD 360 USING FLOATS\n")
print ('Angle','               sin(a)','                       Difference',\
' # of ','  Largest')
print (U"[\N{DEGREE SIGN}" ']','        From math','             From Series'\
,'               terms','   term')

# Calculations.................................................................
angle = 1              
while angle < 2400:
    xx = angle%360 * (math.pi) / 180 # [rads] Only around 360 degrees or 2pi
    value = math.sin(xx)
    xsq = xx**2
    count = 0                      
    total = 0.0
    term = Product = xx
    maxSoFar = 0
    while abs(term) > SMALL:
        maxSoFar =  max(maxSoFar, abs(term))
        total += term
        count += 1
        #print "%4.d %20.16f %20.16f" %(count,term, total)
        Product *= -xsq / (( 2.0 * count) * (2.0 * count + 1))
        term = Product
        difference = total - value
    print ("%4.d  %20.16f %20.16f    %10.3e %3.0i  %10.3g" \
    %(angle, value, total, difference, count, maxSoFar))
    angle+=60
    
print ('\nProgrammed by 'u'\u2606' 'Matt Cann'u'\u2606''\nDate: ',time.ctime(),' \nEnd of processing''\n')
print ('\n')  