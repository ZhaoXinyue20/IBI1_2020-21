# import modules
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import os

# open the xml file
os.chdir("/Users/zhaoxinyue/Documents/GitHub/IBI1_2020-21/Practical14")
DOM = xml.dom.minidom.parse("go_obo.xml")
collection = DOM.documentElement
terms = collection.getElementsByTagName("term")

# create a dictionary to store the GO terms
def dict(terms):
    dict = {}
    for term in terms:
        is_a = [child.childNodes[0].data for child in term.getElementsByTagName("is_a")]
        all_id = term.getElementsByTagName("id")[0].childNodes[0].data
        # children id goes to its father id. if there is no father id existing, add all id.
        for fa_id in is_a:
            if not fa_id in dict:
                dict[fa_id] = [all_id]
            else:
                dict[fa_id].append(all_id)
    return dict

# find id of a specific biomolecules
def gene(terms,molecule):
    gene = []
    for term in terms:
        # search the identified information
        defstr = term.getElementsByTagName("defstr")[0].childNodes[0].data
        id_related = term.getElementsByTagName("id")[0].childNodes[0].data
        if not molecule.isupper():
            defstr = defstr.lower()
        if molecule in defstr:
            gene.append(id_related)
    return set(gene)

# save the childnodes into the all list, and count the childnodes
def getall(dict,lists):
    all = []
    for f in lists:
        if f in dict:
            child = dict[f]
            all += child
            all += getall(dict,child)
    return all

def count_childnodes(terms,molecule):
    dicts = dict(terms)
    match = gene(terms,molecule)
    all_childnodes = getall(dicts,match)
    num = len(set(all_childnodes))
    return num


# the molecules are DNA, RNA, Protein, and Glycoprotein. Use the function and print the results.
DNA = count_childnodes(terms,"DNA")
RNA = count_childnodes(terms,"RNA")
Protein = count_childnodes(terms,"protein")
Glycoprotein = count_childnodes(terms,"glycoprotein")

print("The number of childNodes of all DNA-associated terms is:",DNA)
print("The number of childNodes of all RNA-associated terms is:",RNA)
print("The number of childNodes of all protein-associated terms is:",Protein)
print("The number of childNodes of all glycoprotein-associated terms is:",Glycoprotein)

# make a pie chart
labels='DNA', 'RNA', 'Protein', 'Glycoprotein'
sizes=[DNA, RNA, Protein, Glycoprotein]
explode=(0, 0, 0, 0)
plt.pie(sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        shadow=False,
        startangle=90)
plt.title('the pie chart of the number of childNodes associated with DNA, RNA, protein and glycoprotein')
plt.show()
