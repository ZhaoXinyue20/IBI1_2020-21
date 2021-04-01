import re
import codecs
import os
# read fasta file as a list
infile = input("enter your file address here:")
file=open(infile,"r")
origin = file.readlines()
protein=[]
seq=[]
#translation
genetic_code = {"TTT":"F","TTC":"F","TTA":"L","TTG":"L",
                    "CTT":"L","CTC":"L","CTA":"L","CTG":"L",
                    "ATT":"I","ATC":"I","ATA":"I","ATG":"M",
                    "GTT":"V","GTC":"V","GTA":"V","GTG":"V",
                    "TCT":"S","TCC":"S","TCA":"S","TCG":"S",
                    "CCT":"P","CCC":"P","CCA":"P","CCG":"P",
                    "ACT":"T","ACC":"T","ACA":"T","ACG":"T",
                    "GCT":"A","GCC":"A","GCA":"A","GCG":"A",
                    "TAT":"Y","TAC":"Y","TAA":"STOP","TAG":"STOP",
                    "CAT":"H","CAC":"H","CAA":"Q","CAG":"Q",
                    "AAT":"N","AAC":"N","AAA":"K","AAG":"K",
                    "GAT":"D","GAC":"D","GAA":"E","GAG":"E",
                    "TGT":"C","TGC":"C","TGA":"STOP","TGG":"W",
                    "CGT":"R","CGC":"R","CGA":"R","CGG":"R",
                    "AGT":"S","AGC":"S","AGA":"R","AGG":"R",
                    "GGT":"G","GGC":"G","GGA":"G","GGG":"G"}
for i in range (len(origin)):
	if origin[i].startswith('>'):
		seq.append(origin[i].split(' ')[0])
	else:
		DNA = origin[i].replace('\n', '')
		pro = ''
		for j in range (0, len(DNA), 3): 
			codon = DNA[j:j+3]
			pro += genetic_code[codon]
		protein.append(pro)

# save the new file
fout = codecs.open('protein_unknown_function.fa', "w") 
for i in range(len(seq)):
    fout.write(seq[i])
    fout.write(' ')
    fout.write(str(len(protein[i])))
    fout.write('\n')
    fout.write(protein[i])
    fout.write('\n')
    
fout.close()

