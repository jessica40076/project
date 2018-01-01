import collections

disease=[]
SNPS=[]
beta=[]
merge_disease_SNPS=[]

filename="acess_beta.txt"
input_file = open(filename,"r")
next(input_file)
for line in input_file:
    line=line.strip()
    node=line.split("\t")
    disease.append(str(node[0]))
    SNPS.append(str(node[1]))
    merge_disease_SNPS.append(str(node[0]+'==='+node[1]))
    beta.append(float(node[4]))
input_file.close()

counter=collections.Counter(merge_disease_SNPS)
disease_SNP=list(counter.keys())
values=list(counter.values())

repeat_disease=[]
repeat_SNPS=[]
repeat_count=[]
output_file=[] 
for i in range(len(values)):
    split_result=disease_SNP[i].split("===")
    if values[i]>1:
        repeat_disease.append(split_result[0])  
        repeat_SNPS.append(split_result[1])
        repeat_count.append(values[i])
    else: ## values==1 
        for x in range(len(disease)):
            if disease[x]==split_result[0] and SNPS[x]==split_result[1]:
                 output_file.append(split_result[0]+'\t'+split_result[1]+'\t'+str(beta[x])+'\n')
       
for x in range(len(repeat_disease)):
    value_set=[]
    for y in range(len(disease)):
        if disease[y]==repeat_disease[x] and SNPS[y]==repeat_SNPS[x]:
            value_set.append(beta[y])
            if len(value_set)==repeat_count[x]:
#                output_file.append(disease[y]+'\t'+SNPS[y]+'\t'+str(sum(value_set)/repeat_count[x])+'\n')
#                output_file.append(disease[y]+'\t'+SNPS[y]+'\t'+str(max(value_set))+'\n')
                output_file.append(disease[y]+'\t'+SNPS[y]+'\t'+str(min(value_set))+'\n')

f = open('distinct_by_disease_SNPS_min.txt','w')
f.write("DISEASE/TRAIT\tSNPS\tMEAN\n")
for i in range(len(output_file)):
    f.write(output_file[i])
f.close()     