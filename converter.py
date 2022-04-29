#!/usr/bin/env python3 
# Name: Nathaniel Wolff
# Group Members: None (did alone)

'''
Program docstring goes here
'''
short_AA = {
            'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
            'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
            'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
            'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'
            }

long_AA = {value:key for key,value in short_AA.items()}

RNA_codon_table = {
# Second Base
# U             C             A             G
#U
'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys',
'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',
'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---',
'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Trp',
#C 
'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg',
'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg',
'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',
#A
'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser',
'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',
'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
#G
'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly',
'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly',
'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'
}
#dnaCodonTable = {key.replace('U','T'):value for key, value in rnaCodonTable.items()}

"""We establish several lists which we will iterate through later (the keys, in particular). The first two are not neccessary
but I am again keeping then in here to show that a previous version of this code."""
listOfShortAAValues = list(short_AA.values()) 
listOfRNACodonTableValues = list(RNA_codon_table.values()) 
#print(type(listOfShortAAValues))
listOfKeysShortAA = list(short_AA.keys())
listOfKeysRNA_codon_table = list(RNA_codon_table.keys())

#RNA_codon_table.keys() = keys, still keeping it for records
data = input ("Give the BP codon/AA abbreviation you'd like to look up.")
"""Here is checking if user input is a key. The value will be returned. Otherwise, a for loop 
of all of the keys and their values will be run, and if one is found whos value matches the user input, the codon 
will be displayed."""
if data in short_AA:
    print("Here is the symbol for its corresponding amino acid ="+" " +str(short_AA.get(data)))
elif data in RNA_codon_table:
    print ("Here is the symbol for its corresponding amino acid ="+" " +str(RNA_codon_table.get(data)))
elif data in listOfShortAAValues:
    for i in listOfKeysShortAA:
        if short_AA[i] == data:
            print ("Here is a codon that corresponds to the amino acid ="+" " +str(i))
elif data in listOfRNACodonTableValues:
    for i in listOfKeysRNA_codon_table:
        if RNA_codon_table[i] == data:
            print ("Here is a codon that corresponds to the amino acid ="+" " +str(i))
    
