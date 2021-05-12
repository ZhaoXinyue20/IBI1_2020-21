# Open and read fasta files
f1 = open("/Users/zhaoxinyue/Documents/GitHub/IBI1_2020-21/Practical11/SOD2_human.fa")
f2 = open("/Users/zhaoxinyue/Documents/GitHub/IBI1_2020-21/Practical11/SOD2_mouse.fa")
f3 = open("/Users/zhaoxinyue/Documents/GitHub/IBI1_2020-21/Practical11/RandomSeq.fa")
line1 = f1.readlines()
line2 = f2.readlines()
line3 = f3.readlines()

# save the sequence in lists
SOD2_human=''
SOD2_mouse=''
RandomSeq=''

for i in range (len(line1)):
	if not line1[i].startswith('>'):
		SOD2_human += line1[i].replace('\n','').strip()

for i in range (len(line2)):
	if not line2[i].startswith('>'):
		SOD2_mouse += line2[i].replace('\n','').strip()

for i in range (len(line3)):
	if not line3[i].startswith('>'):
		RandomSeq += line3[i].replace('\n','').strip()

# create the blosum62
amino = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '*']
blosum = [
[ 4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0, -4],
[-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1, -4],
[-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1, -4],
[-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1, -4],
[ 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
[-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1, -4],
[-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
[ 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1, -4],
[-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1, -4],
[-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1, -4],
[-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1, -4],
[-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1, -4],
[-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1, -4],
[-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1, -4],
[-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2, -4],
[ 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0, -4],
[ 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0, -4],
[-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2, -4],
[-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1, -4],
[ 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1, -4],
[-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1, -4],
[-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
[ 0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1, -4],
[-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,  1],
]

# create a function called alignment to get the score
def alignment(s,t,score):
	for i in range (len(s)):
		score=score+blosum[amino.index(s[i])][amino.index(t[i])]
	return score

print('the score of human and mouse is '+str(alignment(SOD2_human,SOD2_mouse,0)))
print('the score of human and random seq is '+str(alignment(SOD2_human,RandomSeq,0)))
print('the score of mouse and random seq is '+str(alignment(SOD2_mouse,RandomSeq,0)))



# separate protein name and sequene
def read(file):
    infile = open(file, "r")
    lines = infile.readlines()
    name = lines[0][1:-1]
    seq = lines[1][:-1]
    return [name, seq]
# extract the sequence 
read("/Users/zhaoxinyue/Documents/GitHub/IBI1_2020-21/Practical11/SOD2_human.fa")
read("/Users/zhaoxinyue/Documents/GitHub/IBI1_2020-21/Practical11/SOD2_mouse.fa")
read("/Users/zhaoxinyue/Documents/GitHub/IBI1_2020-21/Practical11/RandomSeq.fa")

# calculate the percentage of the identical amino acids
def identical_AA(seq1,seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]: # count plus 1 if amino acid is identical
            count += 1
        else:
            count == count
    percent = count/len(seq1)
    percentage = "%.2f%%" % (percent * 100) # reserve two decimal place
    return percentage
# get the percentage
print ("the percentage of identical AA of human and mouse is: " +identical_AA(SOD2_human,SOD2_mouse))
print ("the percentage of identical AA of human adn random seq is: " +identical_AA(SOD2_human,RandomSeq))
print ("the percentage of identical AA of mouse and random seq is: " +identical_AA(SOD2_mouse,RandomSeq))


    


