import collections

disease=[]
filename="acess_beta.txt"
input_file = open(filename,"r")
next(input_file)
for line in input_file:
    node=line.split("\t")
    disease.append(str(node[0]))
input_file.close()

counter=collections.Counter(disease)
disease=list(counter.keys())
values=list(counter.values())

f = open('frequency_calculation.txt','w')
f.write("DISEASE/TRAIT\tfrequency\n")
for i in range(len(disease)):
    f.write(str(disease[i])+'\t'+str(values[i])+'\n')
f.close()     