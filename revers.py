"""This is module docstring"""
import sys


def dna_complement(sequence):
    ''' this is function docstring'''
    sequence = sequence.upper()
    sequence = sequence.replace('A', 't')
    sequence = sequence.replace('T', 'a')
    sequence = sequence.replace('C', 'g')
    sequence = sequence.replace('G', 'c')
    return sequence.upper()


def dna_reverse(sequence):
    ''' this is function docstring'''
    sequence = sequence.upper()
    return sequence[::-1]

DNA = sys.argv[1]
print dna_reverse(DNA)
print dna_reverse(dna_complement(DNA))
