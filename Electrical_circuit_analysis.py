# -----------------------------------------------------------#
# (C) 2020 Matthew Cann
# Released under MIT Public License (MIT)
# email mcann@uwaterloo.ca
# -----------------------------------------------------------

# PURPOSE: Analyze simple electric circuits, both direct current (DC) and 
# alternating current (AC). Using complex numbers for AC circuits   

# Voltage V [Volts]
# Current I [Amperes]
# Resistent R [Ohms]
# Power P [Watts]
# Capactitance C [Farades]
# Frequency Hz [Hertz]

# CIRCUIT EQUATIONS
# V = I*R [V]           -- OHMS LAW
# P = V * I [W]         -- POWER
# P = I**2 * R [W]      -- POWER
# T = RC [Sec]          -- TIME CONSTANT
# I = V/R1 * e**-t/R1*C  [A]--CURRENT
# w = 2 * pi * frequency [rad/sec]-- ANGULAR FREQUENCY
# Xrc = R + (1/jj*w*C) [Ohms]
# I = V/Xrc = (V0 * e ** (j*w*t)) / Xrc

#....................................................................CONSTANTS
OMEGA = U"\N{GREEK CAPITAL LETTER OMEGA}"
MICROFARADES = U"\N{MICRO SIGN}"'F'
MICRO = 1e-6 
SMALL = 1e-18

#......................................................................IMPORTS
import math # not for math.exp
import time
#....................................................................FUNCTIONS
def main():
    print ("EXPLORATION OF SIMPLE CIRCUITS")
    #1
    Volts = getGoodFloat('voltage', 'V', 3, 20)      # [V]Takes user Voltage  
                                                     # assigns to Volts
    Ohms = getGoodFloat('resistance', OMEGA, 5, 1000)# [Ohms]Takes user resistance 
                                                     # assigns it Ohms
    getCurrent_Power(Volts,Ohms) 

    #2 
    Micro_Farades = getGoodFloat('capacitance', MICROFARADES, 50, 10000)
    Farades = Micro_Farades * MICRO           # Converts MicroFarades to Farades
    TConstant = Ohms * Farades                # From T = RC [Sec]

    print ('RC Time Constant: %6.3f [s]' %TConstant  )    # Prints Time Constant
    ttList_1 = getDecayingCurrent(Volts, Ohms, TConstant)# Returns list of times
    final_tt = ttList_1[-1]                    # Takes the last Time in the list

    Ohms2 = Ohms/100.                                # Reduces resistance by 100
    TConstant = Ohms2 * Farades                # Re-Calculates the time constant
    ttList_2 = getDecayingCurrent(Volts, Ohms2, TConstant)# Returns list of times
    final_tt2 = ttList_2[-1]                         # Last time in the list
    print ('\nFinal time for %g[%s]: %5.3f[s]; final time for %g[%s]: %7.5f[s]'\
    %(Ohms,OMEGA, final_tt,Ohms2, OMEGA, final_tt2))

    #3
    Freq = getGoodFloat('frequency', 'Hz', 50, 1000) #[Hz] Assigns input to Freq
    ww_1 = 2 * math.pi * Freq                        # Angular Frequency
    print ('Frequency %d[Hz] corresponds to angular frequency %7.3f[rad/sec]'\
    %(Freq,ww_1))

    max_current_1 = getAlternatingCurrent(Volts, Ohms, Farades, Freq, ww_1)
    # function returns the max current we assign maax_current_1
    Freq_2 = Freq/10.                         # Reduces frequency by 10
    ww_2 = 2 * math.pi * Freq_2               # Angular Frequency
    max_current_2 = getAlternatingCurrent(Volts, Ohms, Farades, Freq_2, ww_2)
    # function returns the max current we assign maax_current_1
    
    C_ratio = max_current_1 / max_current_2   # Finds the ratio of max currents
    print ('\nRatio of peak current at %d[Hz] to peak at %d[Hz] is %7.5f' \
    %(Freq, Freq_2,C_ratio))
    print ('\nProgrammed by 'u'\u2606' 'Matt Cann'u'\u2606''\nDate: ',\
    time.ctime(),' \nEnd of processing''\n'  )
    return 
        
def expSeries(xx):
    """Calculates and returns e**x using a series"""
    count = 0
    term = 1.0
    total = 0.0
    
    while abs(term) > SMALL :
        total += term
        count += 1
        term = term * xx / count
    return total                     # Returns total of expontial series of xx

def getAlternatingCurrent(Volts, Ohms, Cap, ff, ww):
    """Calculates and print a table of voltage and current versus time of two 
    full oscilllations of the volatge
    """
    print ('\nDisplaying alternating voltage and current for:')
    print ('Voltage       %d[V]' %Volts)
    print ('Resistance    %g[%s]' %(Ohms, OMEGA))
    print ('Capacitance   %6.4f[F]' %Cap)
    print ('Frequency     %g[Hz]'%ff)
    
    jj = complex(0,1)
    tt = 0
    ZZ = Ohms + 1/(jj * ww * Cap)
    II = ((Volts * expSeries((jj * ww * tt))/ZZ)).real
    AC_C_List = [II]
    AC_V_List = [Volts]
    ttList = [tt]
    count = 0

    for count in range(24): 
        count += 1 
        tt += ((1./ff) / 12.)
        ttList += [tt]
        Cterm = ((Volts * expSeries((jj * ww * tt))/ZZ)).real
        Vterm = (Volts * expSeries(jj * ww * tt)).real
        AC_V_List += [Vterm]
        AC_C_List += [Cterm]
    
    alist = zip(ttList,AC_V_List, AC_C_List )
    printTable('Time[s]    Voltage[V]    Current[A]', \
    '%7.5f    %9.5f    %9.5f', alist)
    return  max(AC_C_List)

def getCurrent_Power(Volts,Ohms):
    """Calculates and prints table of current flow and power for R/9, R/3, R, 
    3R, and 9R
    """
    RList = [Ohms/9, Ohms/3, Ohms, 3*Ohms, 9*Ohms]
    CList = []      
    CList = [(Volts/term) for term in RList]
    PList = []
    PList = [(Volts * term) for term in CList]
    
    aList = zip(RList, CList , PList)
    
    print ('\nFOR VOLTAGE %g[V]' %Volts)
    printTable('Resistance[%s]    Current[A]    Power[W]' %OMEGA, '%9.2f\t\
    %2.4f\t %7.4f',aList)
    return    

def getDecayingCurrent(Volts, Ohms, TConstant):
    """Calculates and prints table of decaying current flow over time until 
    current drops below 1/1000 of its orginal current
    """
    print ('\nDisplaying decaying current for:')
    print( 'Voltage       %d[V]' %Volts)
    print ('Resistance    %g[%s]' %(Ohms, OMEGA))
    print ('Time constant %g[s]' %TConstant)
    
    tt = 0 #[s]
    term = (Volts / Ohms) * expSeries(-tt/TConstant)
    CapCList = [(Volts / Ohms) * expSeries(-tt/TConstant)]
    ttList = [tt]
    
    while term > (CapCList[0]/1000):
        tt += TConstant/4
        ttList += [tt]
        term = (Volts / Ohms) * expSeries(-tt/TConstant)
        CapCList += [term]
        
    alist = zip(ttList, CapCList)
    (printTable('Time[s]    Current[A]', '%7.5f    %7.5f', alist))
    return ttList            
    
def getGoodFloat(prompt, unit, low, high):
    """Prompts the user for input between guidelines until valid entry is 
    entered"""
    assert(type(low) is float or type(low)is int)
    if low > high:
        low, high = high, low
    errMsg = "\b"                   #Doesnt do anything so we enter the loop
    prompt = "Enter %s between %g[%s] and %g[%s]: "\
    %(prompt, low, unit, high, unit)
        
    while len(errMsg) > 0:
        userInput = input(errMsg + prompt).strip()
        try:
            theResult = float(userInput)
            if not(low <= theResult <= high):
                errMsg = "%g is not between %g and %g," % (theResult, low, high)
            else: errMsg = ""
        except:
            errMsg = "'%s' is not a valid number. " % userInput
    return theResult
    
def printTable(heading, format, aList):
    """Prints table with given heading and format for entries in aList"""
    print (heading)
    for item in aList:
        print (format %item)
    return

#..........................................................................MAIN
main()



 
