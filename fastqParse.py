#!/usr/bin/env python3 
# Name: Nathanie Wolff
# Group Members: “None”

'''
Program docstring goes here.
Idea is the program should take the user's input and slice the input into each of of the types of information as new strings.
Each new string will be assigned to an instance FastqString object, and a method that prints all of its attributes
will be called. 
'''

class FastqString: 

    def __init__(self, inputString): 
        self.inputString = inputString
    
    
    def parse(self):
        splitInputString = self.inputString.split(":")
        Instrument = splitInputString[0]
        Run_ID = splitInputString[1]
        Flow_Cell_ID = splitInputString[2]
        Flow_Cell_Lane = splitInputString[3]
        Tile_Number = splitInputString[4]
        X_Coord = splitInputString[5]
        Y_Coord = splitInputString[6]
        print("Instrument =", Instrument[1:])
        print("Run ID =", Run_ID)
        print("Flow Cell ID =", Flow_Cell_ID)
        print("Flow Cell Lane =", Flow_Cell_Lane)
        print("Tile Number =", Tile_Number)
        print("X-coord =", X_Coord)
        print("Y-coord =", Y_Coord)
        


usersInput = input("Give a fastq sequence to parse that adheres to the given rules.") 
usersFastQSequence = FastqString (usersInput)
usersFastQSequence.parse()



