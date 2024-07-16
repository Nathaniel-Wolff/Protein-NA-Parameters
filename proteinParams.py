aaCompositionNumbers = {'A': 0, 'G':0, 'M':0, 'S':0, 'C': 0, 'H':0,   'N':0 , 'T':0, 'D':0, 'I':0, 'P':0,'V':0, 'E':0,'K':0, 'Q':0, 'W':0, 'F':0,   'L':0,
                              'R':0, 'Y':0 }

aa2mw = {'A': 89.093,  'G': 75.067,  'M': 149.211, 'S': 105.093, 'C': 121.158,
        'H': 155.155, 'N': 132.118, 'T': 119.119, 'D': 133.103, 'I': 131.173,
        'P': 115.131, 'V': 117.146, 'E': 147.129, 'K': 146.188, 'Q': 146.145,
        'W': 204.225,  'F': 165.189, 'L': 131.173, 'R': 174.201, 'Y': 181.189}

mwH2O = 18.015
aa2abs280= {'Y':1490, 'W': 5500, 'C': 125}

aa2chargePos = {'K': 10.5, 'R':12.4, 'H':6}
aa2chargeNeg = {'D': 3.86, 'E': 4.25, 'C': 8.33, 'Y': 10}
aaNterm = 9.69
aaCterm = 2.34

"""Initialization of dictionary that I thought to use, but didn't since I just modified the given dictionary instead with the for loop. This is
a more efficient way of doing this. """
#dictionaryAcidCountsAndMolecularWeights = {}

"""It seemed easier to initialize the pH as part of the class as opposed to passing it as a parameter each time.
Along with protein sequence, the user must then give the pH and the protein sequence to obtain a result."""
class proteinSequences:
    def __init__ (self, proteinSequence, pH):
        self.proteinSequence = proteinSequence
        self.pH = pH

    """Below we establish a dictionary that stores the numbers of AAs in the user's by symbol. We can use this
for later functions, establishing tuple pairs of each count via .items. The functions that use these include 
aaComposition, molar Extinction, and mass Extinction. Other dictionaries are used, but they are all used from their initialized forms."""

    def aaCount (self):
        for i in self.proteinSequence:
            if i in aaCompositionNumbers.keys():
                aaCompositionNumbers[i]+=1
        print("Number of Amino Acids:"+" " +str(len(self.proteinSequence)) )
                #listform = list(aaCompositionNumbers.values())
                #print(type(listform))

    """Here we iterate over each amino acid, and its quantity which we take from the now modified dictionary. We calculate its
    proportion by dividing that qty by the length of the sequence."""
    def aaComposition (self) :
        for aminoAcid, acidCount in aaCompositionNumbers.items():
            print ("The Amino Acid percentages are" + " " + aminoAcid +":"+ str((acidCount/len(self.proteinSequence))*100) + "%")

    """Charge finds the compositions for each of the charged amino acids from the dictionary and multiples them by their charge values 
    found in the charge dictionaries given. It takes the net charge by difference later. Since there are only several charged amino acids, I decided to just store the values in memory
    as opposed to using an iterator or while loop. Since you can't iterate over floating points anyway (which the charges are anyway) it makes
    more sense to do so. """

    def _charge_ (self):
        conditionPH =self.pH
        molesK = aaCompositionNumbers['K']
        molesR = aaCompositionNumbers['R']
        molesH = aaCompositionNumbers['H']
        molesD = aaCompositionNumbers['D']
        molesE = aaCompositionNumbers['E']
        molesC = aaCompositionNumbers['C']
        molesY = aaCompositionNumbers['Y']
        positiveChargeK = float(molesK)*(10.0**float((aa2chargePos)['K'])/(10.0**float((aa2chargePos['K']))+10.0**float(conditionPH)))
        positiveChargeR = float(molesR)*(10.0**float((aa2chargePos)['R'])/(10.0**float((aa2chargePos['R']))+10.0**float(conditionPH)))
        positiveChargeH = float(molesH)*(10.0**float((aa2chargePos)['H'])/(10.0**float((aa2chargePos['H']))+10.0**float(conditionPH)))
        sumOfAllPositiveCharge = positiveChargeK + positiveChargeR + positiveChargeH + aaCterm
        """Here are the negative charges and the sums of all of them."""
        negativeChargeD = float(molesD)*(10.0**float((aa2chargeNeg)['D'])/(10.0**float((aa2chargeNeg['D']))+10.0**float(conditionPH)))
        negativeChargeE = float(molesE)*(10.0**float((aa2chargeNeg)['E'])/(10.0**float((aa2chargeNeg['E']))+10.0**float(conditionPH)))
        negativeChargeC = float(molesC)*(10.0**float((aa2chargeNeg)['C'])/(10.0**float((aa2chargeNeg['C']))+10.0**float(conditionPH)))
        negativeChargeY = float(molesY)*(10.0**float((aa2chargeNeg)['Y'])/(10.0**float((aa2chargeNeg['Y']))+10.0**float(conditionPH)))
        sumOfAllNegativeCharge = negativeChargeD + negativeChargeE + negativeChargeC + aaNterm

        netCharge = sumOfAllNegativeCharge - sumOfAllPositiveCharge
        print("The protein's net charge is" + " " + str(netCharge))


    """This method uses a while loop to iterate through possible pHs and find the one that produces a net charge closest
to zero. It iterates through increments of .01 to get two decimal places of precision. Note that it will display those two places
and the digits after repeat, and shouldn't be taken in the final answer."""
    def pI (self):
            molesK = aaCompositionNumbers['K']
            molesR = aaCompositionNumbers['R']
            molesH = aaCompositionNumbers['H']
            molesD = aaCompositionNumbers['D']
            molesE = aaCompositionNumbers['E']
            molesC = aaCompositionNumbers['C']
            molesY = aaCompositionNumbers['Y']

            netChargeUnderScrutiny = 10000000
            winnerPH = -1.0
            conditionPH = 0.0

            while conditionPH <= 14:
                positiveChargeK = float(molesK)*(10.0**float((aa2chargePos)['K'])/(10.0**float((aa2chargePos['K']))+10.0**float(conditionPH)))
                positiveChargeR = float(molesR)*(10.0**float((aa2chargePos)['R'])/(10.0**float((aa2chargePos['R']))+10.0**float(conditionPH)))
                positiveChargeH = float(molesH)*(10.0**float((aa2chargePos)['H'])/(10.0**float((aa2chargePos['H']))+10.0**float(conditionPH)))
                sumOfAllPositiveCharge = positiveChargeK + positiveChargeR + positiveChargeH + aaCterm
                negativeChargeD = float(molesD)*(10.0**float((aa2chargeNeg)['D'])/(10.0**float((aa2chargeNeg['D']))+10.0**float(conditionPH)))
                negativeChargeE = float(molesE)*(10.0**float((aa2chargeNeg)['E'])/(10.0**float((aa2chargeNeg['E']))+10.0**float(conditionPH)))
                negativeChargeC = float(molesC)*(10.0**float((aa2chargeNeg)['C'])/(10.0**float((aa2chargeNeg['C']))+10.0**float(conditionPH)))
                negativeChargeY = float(molesY)*(10.0**float((aa2chargeNeg)['Y'])/(10.0**float((aa2chargeNeg['Y']))+10.0**float(conditionPH)))
                sumOfAllNegativeCharge = negativeChargeD + negativeChargeE + negativeChargeC + aaNterm
                netCharge = sumOfAllNegativeCharge - sumOfAllPositiveCharge
                if netCharge < netChargeUnderScrutiny:
                    winnerPH = conditionPH
                    netChargeUnderScrutiny = netCharge
                conditionPH +=.01
            print("The ideal pH for the isoelectric point is"+ " " + str(winnerPH))


                    #print("The isoelectric point is" + str(conditionPH))


    #note that Tyrosine is Y, W is tryptophans, C is cysteines
    # we need to refernce the modified dictionary
    """Here we do use an iterator to find the amino acid numbers for the ME coefficient relevant acids. There aren't any floating points to 
    iterate over, just strings, so this works. The initialized acidCount objects are used to calculate the final value."""

    def molarExtinction (self):
        acidCountsY = 0
        acidCountsW = 0
        acidCountsC = 0
        molarExtinctionY = 0
        molarExtinctionW = 0
        molarExtinctionC = 0
        for symbols, acidCounts in aaCompositionNumbers.items():
            if symbols  == 'Y':
                acidCountsY = acidCounts
            elif symbols == 'W':
                acidCountsW = acidCounts
            elif  symbols == 'C':
                acidCountsC = acidCounts
        for otherSymbols, aa2abs280specific in aa2abs280.items():
             if otherSymbols  == 'Y':
                molarExtinctionY = aa2abs280specific
             elif otherSymbols  == 'W':
                molarExtinctionW = aa2abs280specific
             elif otherSymbols  == 'C':
                molarExtinctionC = aa2abs280specific
        finalMolarExtiction = float(acidCountsY*molarExtinctionY)+float(acidCountsW*molarExtinctionW)+float(acidCountsC*molarExtinctionC)
        print("The Molar Extinction Coefficient is" + " " + str(finalMolarExtiction))
    """Molecular Weight uses the counts of amino acid modified dictionary to caulate the molecular weight using a while loop to calculate each
    mass contribution of individual amino acid, and later add them together. """
    def molecularWeight (self):
        listOfMolarWeights = list(aa2mw.values())
        listOfAcidCounts = list(aaCompositionNumbers.values())
        listofMolarContributionsAA = []
        i = 0
        while i <= 19:
            molarContributionAA = listOfAcidCounts[i]*(listOfMolarWeights[i]-(mwH2O))
            listofMolarContributionsAA.append(molarContributionAA)
            i+=1
            totalMolarMass = sum(listofMolarContributionsAA) + mwH2O
        print("The protein's Molar Mass is" + " " + str(totalMolarMass))

    """In order to redefine the molar weight and the ME coefficient, I copied and pasted that code into this method. If there are other ways 
    to store it in memory, I am not sure of them, and since the code was already written, it is not strictly neccessary to come up with a different 
    way of gathering the answer."""
    def massExtinction (self):
        acidCountsY = 0
        acidCountsW = 0
        acidCountsC = 0
        molarExtinctionY = 0
        molarExtinctionW = 0
        molarExtinctionC = 0
        for symbols, acidCounts in aaCompositionNumbers.items():
            if symbols  == 'Y':
                acidCountsY = acidCounts
            elif symbols == 'W':
                acidCountsW = acidCounts
            elif  symbols == 'C':
                acidCountsC = acidCounts
        for otherSymbols, aa2abs280specific in aa2abs280.items():
             if otherSymbols  == 'Y':
                molarExtinctionY = aa2abs280specific
             elif otherSymbols  == 'W':
                molarExtinctionW = aa2abs280specific
             elif otherSymbols  == 'C':
                molarExtinctionC = aa2abs280specific
        finalMolarExtiction = float(acidCountsY*molarExtinctionY)+float(acidCountsW*molarExtinctionW)+float(acidCountsC*molarExtinctionC)
        listOfMolarWeights = list(aa2mw.values())
        listOfAcidCounts = list(aaCompositionNumbers.values())
        listofMolarContributionsAA = []
        i = 0
        while i <= 19:
            molarContributionAA = listOfAcidCounts[i]*(listOfMolarWeights[i]-(mwH2O))
            listofMolarContributionsAA.append(molarContributionAA)
            i+=1
            totalMolarMass = sum(listofMolarContributionsAA) + mwH2O
        massExtinctionCoeff= finalMolarExtiction / totalMolarMass
        print("The Mass Extinction Coefficient is" + " " + str(massExtinctionCoeff))

userInputProteinSequence = input("Give the protein sequence you'd like to analyze.")
usersPH = input("Give the pH the protein is in.")
userInputProteinSequenceUpperCase=userInputProteinSequence.upper()

usersProteinObject = proteinSequences(userInputProteinSequenceUpperCase, usersPH)
usersProteinObject.aaCount()
usersProteinObject.molarExtinction()
usersProteinObject.massExtinction()
usersProteinObject.aaComposition()
usersProteinObject.molecularWeight()
usersProteinObject._charge_()
usersProteinObject.pI()


