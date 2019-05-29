""" All tasks come from www.codewars.com """

"""
TASK: Complementary DNA

Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" 
for the development and functioning of living organisms.

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. 
DNA strand is never empty or there is no DNA at all (again, except for Haskell).

Examples:
DNA_strand ("ATTGC") # return "TAACG"
DNA_strand ("GTAT") # return "CATA"
"""


def DNA_strand(dna):
    dna_sequence = {"A":"T",
                    "T":"A",
                    "C":"G",
                    "G":"C"
                    }
    return "".join([dna_sequence[x] for x in dna])

