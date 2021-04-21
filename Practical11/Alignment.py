#BLOSUM62 score
from Bio.Align import substitution_matrices
from Bio import pairwise2
from Bio import SeqIO

blosum62 = substitution_matrices.load("BLOSUM62")
# read the files
human = SeqIO.read("/Users/zhaoxinyue/Documents/GitHub/IBI1_2020-21/Practical11/SOD2_human.fa", "fasta")
mouse = SeqIO.read("/Users/zhaoxinyue/Documents/GitHub/IBI1_2020-21/Practical11/SOD2_mouse.fa", "fasta")
random = SeqIO.read("/Users/zhaoxinyue/Documents/GitHub/IBI1_2020-21/Practical11/RandomSeq.fa", "fasta")
# get the alignment score
human_mouse = pairwise2.align.globalds(human.seq, mouse.seq, blosum62, -10, -0.5)
human_random = pairwise2.align.globalds(human.seq, random.seq, blosum62, -10, -0.5)
mouse_random = pairwise2.align.globalds(random.seq, mouse.seq, blosum62, -10, -0.5)
# /show the alignment score and the sequence/
print(human_mouse)
print(human_random)
print(mouse_random)


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

# copy the sequence from the output of the read function 
human = "MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"
mouse = "MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"
random = "WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL"

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
identical_AA(human,mouse)
identical_AA(human,random)
identical_AA(mouse,random)


    


