Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#!/usr/bin/env python3 
# Name: Nathaniel Wolff  
# Group Members: "None”

'''
Read a DNA string from user input and return a collapsed substring of embedded Ns to: {count}.

"""Overview: Here, the program takes the user's DNA sequence and passes to an instance of the DNAString class as an 
attribute. A method for this class called purify that counts the Ns and replaces them with a bracketed number is 
then called to that instance and printed."""

Example: 
 input: AaNNNNNNGTC
output: AA{6}GTC

Any lower case letters are converted to uppercase
'''

""" Here the DNAString class is initialized, and inherits the string methods as well."""
""" The setup for the DNAstring class is here. """
class DNAstring (str):
    def __init__(self, userDNASequence):
        self.userDNASequence = userDNASequence #one of the attributes of the DNAsequenceclass is userDNASequence. 
       
    """Length method is just another way of assigning the len function as a method of the class for us to call. Not
needed, but I kept it here in case I ever use parts of this code again and need string length."""
    def length(self):
        return len(self)
    
    """Here is the method that will be called upon to delete the Ns and replace them with their count."""
    def purify(self): 
        ''' Return an upcased version of the string, collapsing a single run of Ns.''' #aswrittenabove
        upCase = self.upper()#this method gives the uppercase of the passed object as a stylistic choice
        leftIndex = upCase.find('N') #.find gives first index of argument, N in this case in the upCased"d" argument
        ns = upCase.count('N') #counts all occurences of the argument in the passed object
        pureDNA = upCase #new value of the object: pureDNA, which will be the upCase result, I dont think we need this anyway
        if ns >= 1: 
            right = upCase[leftIndex+ns :] #new list is formed that starts from the ns+left index and goes to the end
            pureDNA = upCase[:leftIndex] + '{' + str(ns) + '}' + right
        else:
            pureDNA = upCase
        return pureDNA 
        
"""If, else statement is used here to construct a new string with the Ns integrated inside the new string
        a as a count. Else will return the original string, if the condition of no ns is met."""
        


"""Here we take the DNA sequence as input, assign it to the userDNASequence attribute of an instance of 
the class, and print the result of the purify method."""

rawDNASequenceFromUser = input("Give a DNA sequence")

usersDNA = DNAstring(rawDNASequenceFromUser)
print(usersDNA.purify())
