import re
import codecs
import os
# read fasta file as a list
os.chdir("/Users/zhaoxinyue/Documents/GitHub/IBI1_2020-21/Practical8")
file=open("unknown_function.fa","r")
origin = file.readlines()
protein=[]
seq=[]

#translation
# give the codon table
genetic_code = {'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L',
'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',
'TAT':'Y', 'TAC':'Y', 'TAA':'O', 'TAG':'U',
'TGT':'C', 'TGC':'C', 'TGA':'X', 'TGG':'W',
'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Z',
'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
'ATT':'I', 'ATC':'I', 'ATA':'J', 'ATG':'M',
'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'AAT':'N', 'AAC':'B', 'AAA':'K', 'AAG':'K',
'AGT':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}

for i in range (len(origin)):
	if origin[i].startswith('>'):
		seq.append(origin[i].split(' ')[0]) # get the sequence
	else:
		DNA = origin[i].replace('\n', '') 
		pro = ''
		for j in range (0, len(DNA), 3):  # read the codons
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
