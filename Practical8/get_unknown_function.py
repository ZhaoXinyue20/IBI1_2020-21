import os
import re
import codecs
# read fasta file as a list
os.chdir("/Users/zhaoxinyue/Documents/GitHub/IBI1_2020-21/Practical8")
file=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
origin = file.readlines()
output = []
#find unknow function DNA and extract them
for i in range(len(origin)):
    if origin[i].startswith('>') and re.search(r'unknown function', origin[i]):               
        name=re.search(r'(>.+?)_',origin[i])
        Name=name.group()
        output.append(Name)            
        a = ''
        for j in range(len(origin[i:-1])):
            if origin[i+j+1].startswith('>'): 
              break
            else:
              a += origin[i+j+1][:-1]
        a += "\n"
        output.append(a)
# get the length of the gene
        length = ''
        output.append(length)
for i in range(len(output)):
    if output[i].startswith('>'):
        length=str(len(output[i+1])-1)
        output[i] += "  "
        output[i] += length + "\n"

# save the new file
fout = codecs.open('unknown_function.fa', "w") 
for i in output:
    fout.write(i)
fout.close()
