#..............................................................................
# (C) 2020 Matthew Cann
# Released under MIT Public License (MIT)
# email mcann@uwaterloo.ca
#..............................................................................
# PURPOSE: To count the number of valid 5-character passwords following certain
# rules.
#.......................................................................IMPORTS
import numpy as np
import time
#.....................................................................CONSTANTS
PW_LEN= 5

#.....................................................................FUNCTIONS
def main():
    """main() does nothing
    the main function of the script
    """
    print ("PROGRAM TO COUNT VALID PASSWORDS")
    numLetters = getBoundedInt(1, 26, "Enter a number of letters:")
    numDigits = getBoundedInt(1,10, "Enter the number of digits:")
    upper = genString( 'A', numLetters)
    lower = genString('a', numLetters)
    digits = genString('0', numDigits)
    LETTERS = digits+upper+lower
    codedArray = genArray(PW_LEN,LETTERS)
    if len(LETTERS) <= 5:
        genGoodPasswords(LETTERS)
    else:
        print ('All characters in passwords:',(LETTERS))
        print ('\nDate:',time.ctime())
        #print genGoodPasswords(LETTERS)
        totalgoodPW = 0
        totalPW = 0
        print ("Progress indictor")
        for num in range(len(LETTERS)):
            term = LETTERS[num] 
            print (term)
            
            codedArray[ : ,0] = num
            num_goodPW = 0
            num_goodPW = checkPasswords(codedArray,numLetters,numDigits)
            totalgoodPW += num_goodPW   
            totalPW += np.sum(np.shape(codedArray), axis = 0) 
        print ("The total number of passwords is %d out of %d"%(totalgoodPW, totalPW))
        print ('\nProgrammed by 'u'\u2606' 'Matt Cann'u'\u2606''\nDate: ',\
        time.ctime(),' \nEnd of processing''\n'  )
    return 

#..........................................     
def checkPasswords(codedArray, numLetters, numDigits):
    '''This function tests the 
passwords represented by the numbers in codedArray and determines how many pass 
all the rules
'''
    count = 0 #number of good passwords
    
    #at least one digit
    num_Digits = np.sum(codedArray < numDigits, axis = 1)
    checkDigits = num_Digits > 0

    #at least one lowercase letter
    num_Lcase = np.sum(codedArray >= (numDigits+numLetters), axis = 1)
    checkLowercase = num_Lcase > 0
    
    #at least one uppercase
    numUcase = PW_LEN - num_Digits - num_Lcase
    checkUppercase = numUcase > 0
    
    # no character can appear twice in a row
    col0 = codedArray[:,0]
    col1 = codedArray[:,1]
    col2 = codedArray[:,2]
    col3 = codedArray[:,3]
    col4 = codedArray[:,4]
    bol_array = (col0 !=col1) * (col1 != col2) * (col2!=col3) * (col3 != col4)
    
    count = np.sum(checkLowercase * checkDigits * bol_array* checkUppercase )
    return count

            
#...........................................
def genArray(numPwChars,LETTERS):
    '''This function returns an n^m-1 × m 2-dimensional array of int8 codes 
    representing all variations of the last m-1 characters
    '''
    nn=len(LETTERS)
    numRows = nn**(PW_LEN-1)
    array = np.zeros( (numRows, numPwChars),dtype=np.int8)
    array[:,4] = np.resize(np.arange(nn), (numRows))
    array[:,3] = np.resize(np.repeat((np.arange(nn)),nn,axis=0), (numRows))
    array[:,2] = np.resize(np.repeat((np.arange(nn)),nn**2,axis=0), (numRows))
    array[:,1] = np.resize(np.repeat((np.arange(nn)),nn**3,axis=0), (numRows))
    return array 
#........................................
def genGoodPasswords(LETTERS):
    '''Finds all possible passwords, then tests them and returns a list of the 
    ones that pass all the tests.
    '''
    UPPER = genString( 'A', 26)
    LOWER = genString('a', 26)
    DIGITS = genString('0', 10)
    print ("\nAll characters in passwords:", (LETTERS))
    print ('\nDate:',time.ctime())
    passwords = ["".join((c0, c1, c2, c3, c4))
    for c0 in LETTERS
        for c1 in LETTERS
            for c2 in LETTERS
                for c3 in LETTERS
                    for c4 in LETTERS]
                    
    goodPasswords = []
    for password in passwords:   
        #for Uletter in upper:
        ULetters = [[(Uletter == char)for char in password]for Uletter in UPPER]
        hasUpper = np.sum(ULetters) >=1 
        if hasUpper == True:
            LLetters = [[(Lletter == char) for char in password]for Lletter in LOWER]
            hasLower = np.sum(LLetters) >= 1
            if hasLower == True:
                num_Digits = [[(dig == char) for char in password]for dig in DIGITS]
                hasDigit = np.sum(num_Digits) >= 1
                if hasDigit == True:
                    prev= ' '
                    pairs = 0
                    for char in password:
                        pairs += prev == char
                        prev = char
                    check3 = (pairs == 0)
                    goodPasswords += [password] * check3
    print ("\nThere are %g good passwords:" %len(goodPasswords))
    print ('\n',goodPasswords)
    print ("\nThe total number of good passwords is %g out of generated %g"\
    %(len(goodPasswords), len(passwords)))
    print ('\nProgrammed by 'u'\u2606' 'Matt Cann'u'\u2606''\nDate: ',\
    time.ctime(),' \nEnd of processing''\n')
    return 

#.......................................  
def genString(firstCh, numCh):
    '''This function returns a string containing numCh consecutive 
characters from firstCh on
'''
    return ''.join([chr(xx) for xx in range(ord(firstCh),
            ord(firstCh) + numCh)])
#.............................................        
    
def getBoundedInt(low, high, prompt):
    """Prompts the user for input between guidelines until valid entry is 
    entered or the user tried 3 times where the closest limit is chosen from 
    their last pick"""
    assert(type(low) is float or type(low)is int)
    if low > high:
        low, high = high, low
    errMsg = "\b"                   #Doesnt do anything so we enter the loop
    prompt += " (%d - %d) " %(low, high)
    tries = 0
    while len(errMsg) >0 and tries < 3:
        userInput = input(prompt).strip()
        tries += 1 
        try:
            theResult = int(userInput)
            if not(low <= theResult):
                if theResult < low:
                    limit = "Low"
                errMsg = "\nInput value %g is too %s" % (theResult, limit)
                print  (errMsg)
                
            elif not(theResult <= high):
                if theResult > high:
                    limit = "High"
                errMsg = "\nInput value %g is too %s" % (theResult, limit)
                print  (errMsg)
            
            else:
                errMsg = ""
        except:
            errMsg = "'%s' is not a valid number." % userInput
            print (errMsg)
    if tries == 3:
        if theResult > high:
            theResult = high
        elif theResult < low:
            theResult = low 
    print ("Using",theResult    )  
    return theResult
    
#..........................................................................MAIN
     
     
main()


 



 


      






