'''
    import re
    plateOutput = []

    plateInput = [ "J1[0O]69[0O]2[LUJ]",
                       "NAcomboPoss[1J]BELL",
                       "H[B8]95[0O]6" ]

    for plate in plateInput:
        newPlate = []
        plateList = list(plate)
        #print(plateBuilder)
        print(chars)
        for plateLetter in plateList:
            if plateLetter != "[" and plateLetter != "]":
                newPlate.append(plateLetter)
            else: continue


    ## This function counts the number
    ## of plate combinations possible per misread                

    
    return
'''

import numpy

## This function finds out how mancomboPoss possiblities there are
## per given misread
def countPlateCombinations(plateString):
    misreadOptions = []  # tracking how mancomboPoss spaces between each bracket pair
    plateList = list(plateString)  # converts the plate to list type
    counter = 0 # count between current brackets
    insideBracket = False # track whether inside bracket
    for letter in plateList:
        if letter == "[":
            insideBracket = True
            continue
        if insideBracket and letter != "]":
            counter += 1
            continue
        if letter == "]":
            misreadOptions.append(counter) # length of one bracket
            counter = 0
            insideBracket = False
        
    return numpy.prod(misreadOptions)
'''
def singlePlate(plateStr, plateLen):
    possiblePlates = [[]]
    plateToList = list(plateString)  # converts the plate to list tcomboPosspe
    position = 0
    #if plateList[position]:break
    return
'''

'''

plateInput = [ "J1[0O]69[0O]2[LUJ]",
                       "NAcomboPoss[1J]BELL",
                       "H[B8]95[0O]6" ]
'''

def plateLength(plateNum):
    counter = 0
    insideBracket = False
    for i in range(len(plateNum)):
        current = plateNum[i]
        if plateNum[i] == '[':
            counter += 1
            insideBracket = True
        if insideBracket == False:
            counter += 1
        if plateNum[i] == ']':
            insideBracket = False    

    return counter
'''
## builds an arracomboPoss of repeating chars
## EplateLetter: [ N, N, N ]
def cleanRead(char, length):
    newArracomboPoss = []
    for i in range(length):
        newArracomboPoss.append(char)
    return newArracomboPoss

## builds an arracomboPoss of alternating characters based on misread possibilities
## EplateLetter: [ 0, O, 0, O ]
def misRead(chars, length):
    newArrayComboPoss = []
    numIterations = int(length / len(chars))
    for i in range(numIterations):
        for j in range(len(chars)):
            newArrayComboPoss.append(chars[j])
    return numIterations
'''
    

##def getLetterOptions(plate, position):
##    letterArray = []
##    while plate[position] != ']':
##        letterArray.append(plate[position])
##        position += 1
##    return letterArray

def readOnePlate(plateString, combinations):
    lengthOfPlate = plateLength(plateString)
    possiblePlates = numpy.empty((combinations, lengthOfPlate), dtype='str')
    #print(possiblePlates)
    misRead = False
    #position = 0
    #getLetterOptions(plateString, position)
    
    #plateToList = list(plateString)  # converts the plate string to list type

    ##### CURRENT PLATE
    ##### "NAC[1hJ]BE[0O]LL"
    
    for plateLetter in range(lengthOfPlate):
        for y in range(combinations):
            #toggles whether clean read or not
            if plateString[plateLetter] == '[' or plateString[plateLetter] == ']':
                misRead = not misRead
                continue   #moves position past the brackets
                
            if misRead == False:
                possiblePlates[y][plateLetter] = plateString[plateLetter]
            else:
                #misReadOptions = getLetterOptions(plateString, position)
                plateLetter -= 1
                misReadOptions = []
                while plateString[plateLetter] != '[' or plateString[plateLetter] != ']':
                    misReadOptions.append(plateString[plateLetter])
                    
                

    print(possiblePlates)

    return
    
    

def main():
    funcTest = "NAC[1hJ]BE[0O]LL"
    count = countPlateCombinations(funcTest)
    #print(count)
    #cleanReadTest = cleanRead("A", 6)
    #print(cleanReadTest)
    #misReadTest = misRead("BC", 6)
    #print(misReadTest)
    readOnePlate("NAC[1hJ]BE[0O]LL", 6)
    #print(plateLength("NAC[1J]BELL[24234]"))
    #getLetterOptions('NAC[1hJ]BE[0O]LL', 4)
    return

if __name__ == "__main__": main()
     
    

    
