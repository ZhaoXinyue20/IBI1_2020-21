import matplotlib.pyplot as plt
import numpy as np
# set two lists
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
gene_lengths=np.array(gene_lengths)
exon_counts=np.array(exon_counts)
average_length=gene_lengths/exon_counts
# change array to list
average_lengths=list(average_length)
# sort lengths
average=sorted(average_lengths)
print ("the average lengths are:" + str(average))
# make a boxplot
n = 10
score = average_lengths
plt.boxplot(score,
            vert=True, #boxplot is vertically presented
            whis=1.5, #specifies how far the upper and lower quartiles must be from the upper and lower quartiles. 
            patch_artist=True, #the boxplot has color
            meanline=False, #the mean as a line
            showbox=True, #presented as a box
            showcaps=True, #two lines at the top and end
            notch=False #no notches
            )
plt.title('the distribution of the average exon length')
plt.show()
