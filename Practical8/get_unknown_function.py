import os
import re
import codecs
# read fasta file as a list
os.chdir("/Users/zhaoxinyue/Documents/GitHub/IBI1_2020-21/Practical8")
file=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
lines = file.readlines()

output = []
for i in range(len(lines)):
    if lines[i].startswith(">") and "unknown function" in lines[i]:
        # get the name using regular expresion
        output.append(re.findall(r'(>.+?)(?:_)', lines[i])[0])
        a = ""
        # add the line(sequence) until next name appear
        for j in range(len(lines[i:-1])):
            if lines[i+j+1].startswith(">"):
                break
            else:
                a += lines[i+j+1][:-1]
        a += "\n"
        output.append(a)

# add lengths of the sequence
for i in range(len(output)):
    if output[i].startswith(">"):
        output[i] += "  "
        output[i] += str(len(output[i+1])-1)
        output[i] += "\n"

# save the new file
fout = codecs.open('unknown_function.fa', "w") 
for i in output:
    fout.write(i)
fout.close()
