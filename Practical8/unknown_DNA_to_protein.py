import re
import codecs
import os

# make translation function  
def translation(gene):
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
    protein = ""
    for i in range (0, len(gene),3):
        codon = origin[i:i+3]
        if genetic_code[codon] != "STOP":
            protein += genetic_code [codon]
        else:
            break
    print(protein)

# read fasta file as a list
INPUT = input("enter your file address here:")
file=open(INPUT,"r")
origin = file.readlines()
# set some variable to temporarily put things
output = []
Len=''
data=""
result = []
#find unknow function DNA and extract them
for i in range(len(origin)):
    if origin[i].startswith('>') and re.search(r'unknown function', origin[i]):               
        name=re.search(r'(>.+?)_',origin[i])
        Name=name.group()
        output.append(Name)
        exp = ''            
        a = ''
        exp += '\n'
        for j in range(len(origin[i:-1])):
            if origin[i+j+1].startswith('>'): 
              break
            else:
              a += origin[i+j+1]
        exp +=a .replace('\n','')
        output.append(exp)
        
# !translation and get the protein length
pro = []
for line in output:
    if line.startswith(">"):
        pro.append(line)
    else:
        pro.append(translation(line))

for x in range(len(output)):
    if pro[x].startswith(">"):
        pro[x] = re.search(r'>.+?',output[x])
        pro[x] +=str(len(pro[x+1]))
        pro[x] +="\n"
    else:
        break

# save the new file
fout = codecs.open('unknown_function_protein.fa', "w") 
for line in pro:
    fout.write(line)
fout.close()

