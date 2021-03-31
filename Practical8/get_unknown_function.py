import os
import re
import codecs
# read fasta file as a list
os.chdir("/Users/zhaoxinyue/Documents/GitHub/IBI1_2020-21/Practical8")
file=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
origin = file.readlines()
# set some variable to temporarily put things
output = []
Len=''
data=""

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

# then count the length of the gene
        Len = ''   
        output.append(Len)

for i in range(len(output)): 
    if output[i].startswith('>'):
        Len=str(len(output[i+1])-1)
        output[i+2]+= '\n' + Len + '\n' # I put the length at the last line
        
# save the new file
fout = codecs.open('unknown_function.fa', "w") 
for line in output:
    fout.write(line)
fout.close()


                

