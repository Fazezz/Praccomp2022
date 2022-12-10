#! /urs/bin/env python
#DNASeq = 'ATCGATCGATCG'

DNASeq = input('Enter a DNA sequence: ').upper()
#DNASeq = DNASeq.upper()
DNASeq = DNASeq.replace(' ', '')

print('\n\nSequence: ', DNASeq)

SeqLenght = float(len(DNASeq))

print('Sequence Lenght: ', SeqLenght, '\n')

NumberA = DNASeq.count('A')
NumberC = DNASeq.count('C')
NumberG = DNASeq.count('G')
NumberT = DNASeq.count('T')

print('A: ',NumberA/ SeqLenght)
print('C: ',NumberC/ SeqLenght)
print('C: ',NumberG/ SeqLenght)
print('T: ',NumberT/ SeqLenght)

TotalStrong = NumberC + NumberG
TotalWeak = NumberA + NumberT

#Sequence has different properties after 14 nucleotides

if SeqLenght > 14:

	MeltTemp = (4 * TotalStrong) + (2 * totalWeak)
	print('Melting Temp: , MeltTemp (short): ', MeltTemp, ' C\n')
else
	MeltTempLong = 64.9 + 41 * (TotalStrong - 16.4) / SeqLenght
	print('Melting Temp: MeltTemp (long): ' ,MeltTempLong, 'C\n')
BaseList = 'ATCG'

for Base in BaseList:
	Percent = 100 *DNASeq.count(Base) / SeqLenght
	print(Base, Percent, '%\n')

Comp=DNAseq.replace('A', 't')
Comp=DNAseq.replace('T', 'a')
Comp=DNAseq.replace('C', 'g')
Comp=DNAseq.replace('G', 'g')

print('Thecomplimentary sequence is: ', Comp, '\n')
print('The reverse compliment is: ', Comp[::-1], '\n')

print('\n')

#print('\n Melting Temp (long): ', MeltTempLong, 'C')
