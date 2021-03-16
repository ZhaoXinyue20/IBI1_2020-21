# sorting lists
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
# sorted values for the average exon length across 10 genes
gene_lengths.sort()
# make boxplot
n = 10
score = gene_lengths
plt.boxplot(score, vert=True,whis=1.5,patch_artist=True, meanline=False, showbox=True, showcaps=True, notch=False)
plt.show()
