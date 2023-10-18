# Morse Code dictionary for letters
morseDict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J','-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T','..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',}
currentIteration = []
combinations = []
convertedCombinationList = []

def createDivisions(n, currentIteration, combinations):
    # creates list of possible divisions of the string by dividing the lenght of the string to 1,2,3 and 4
    if n == 0:
        combinations.append([i for i in currentIteration]) 
        return
    for i in range(1, min(n+1, 5)): 
        currentIteration.append(i)
        createDivisions(n - i, currentIteration, combinations)
        currentIteration.pop()

def convertMorse(string,stringCombination):
    # Creates the converted stings by dividing the input strings based on the number combinations then converting each substring into a letter
    output = ""
    if len(string)==0:
        if "1" in output:
            print("1 in output")
            return
        return output
    if morseDict.get(string[0:stringCombination[0]]):
        output =  morseDict.get(string[0:stringCombination[0]]) + convertMorse(string[stringCombination[0]:], stringCombination[1:]) 
    else:
        # If a string of morse code isn't found from the dictionary, it will instead convert it to "1" 
        output = "1"
    return output


# Sample input from the problem description
inputString = '-..-----.'
stringLength = len(inputString)
createDivisions(stringLength, currentIteration, combinations)
    

for i in combinations:
    convertedCombinationList.append(convertMorse(inputString,i))

# Correct output based on the problem description
outputList = [
    "XOTE", "XON", "XTOE", "XTTG", "XTTTTE", "XTTTN", "XTTME", "XTMTE", "XTMN", "XMG", "XMTTE", "XMTN", "XMME",
    "TIOG", "TIOTTE", "TIOTN", "TIOME", "TITOTE", "TITON", "TITTOE", "TITTTG", "TITTTTTE", "TITTTTN", "TITTTME", "TITTMTE", "TITTMN", "TITMG", "TITMTTE", "TITMTN", "TITMME",
    "TIMOE", "TIMTG", "TIMTTTE", "TIMTTN", "TIMTME", "TIMMTE", "TIMMN",
    "TEWOE", "TEWTG", "TEWTTTE", "TEWTTN", "TEWTME", "TEWMTE", "TEWMN", "TEAOTE", "TEAON", "TEATOE", "TEATTG", "TEATTTTE", "TEATTTN", "TEATTME", "TEATMTE", "TEATMN", "TEAMG", "TEAMTTE", "TEAMTN", "TEAMME",
    "TEEOG", "TEEOTTE", "TEEOTN", "TEEOME", "TEETOTE", "TEETON", "TEETTOE", "TEETTTG", "TEETTTTTE", "TEETTTTN", "TEETTTME", "TEETTMTE", "TEETTMN", "TEETMG", "TEETMTTE", "TEETMTN", "TEETMME",
    "TEEMOE", "TEEMTG", "TEEMTTTE", "TEEMTTN", "TEEMTME", "TEEMMTE", "TEEMMN", "TEJG", "TEJTTE", "TEJTN", "TEJME",
    "TUOTE", "TUON", "TUTOE", "TUTTG", "TUTTTTE", "TUTTTN", "TUTTME", "TUTMTE", "TUTMN", "TUMG", "TUMTTE", "TUMTN", "TUMME",
    "DOG", "DOTTE", "DOTN", "DOME", "DTOTE", "DTON", "DTTOE", "DTTTG", "DTTTTTE", "DTTTTN", "DTTTME", "DTTMTE", "DTTMN", "DTMG", "DTMTTE", "DTMTN", "DTMME",
    "DMOE", "DMTG", "DMTTTE", "DMTTN", "DMTME", "DMMTE", "DMMN",
    "NWOE", "NWTG", "NWTTTE", "NWTTN", "NWTME", "NWMTE", "NWMN", "NAOTE", "NAON", "NATOE", "NATTG", "NATTTTE", "NATTTN", "NATTME", "NATMTE", "NATMN", "NAMG", "NAMTTE", "NAMTN", "NAMME",
    "NEOG", "NEOTTE", "NEOTN", "NEOME", "NETOTE", "NETON", "NETTOE", "NETTTG", "NETTTTTE", "NETTTTN", "NETTTME", "NETTMTE", "NETTMN", "NETMG", "NETMTTE", "NETMTN", "NETMME",
    "NEMOE", "NEMTG", "NEMTTTE", "NEMTTN", "NEMTME", "NEMMTE", "NEMMN",
    "NJG", "NJTTE", "NJTN", "NJME"
]
# removes the strings with invalid combinations which will be indicated with a "1" in the string
convertedCombinationList = [x for x in convertedCombinationList if "1" not in x]

print("\n\nList of letter combinations generated: \n")
print(convertedCombinationList)

# For checking if output is correct
missingEntries = [x for x in outputList if x not in convertedCombinationList] # Check if there are missing entries
extraEntries = [x for x in convertedCombinationList if x not in outputList] # Check if there are extra entries
if (missingEntries == [] and extraEntries == []):
    print("\n\nOutput is correct and Validated")