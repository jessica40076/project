from IPython import get_ipython
get_ipython().magic('reset -sf')

disease=[]
SNPS=[]
beta=[]
SNP_score={}
filename="distinct_by_disease_SNPS_mean.txt"
input_file = open(filename,"r")
next(input_file)
for line in input_file:
    line=line.strip()
    node=line.split("\t")
    disease.append(str(node[0]))
    SNPS.append(str(node[1]))
    beta.append(float(node[2]))
    SNP_score[str(node[1])]=float(node[2])
input_file.close()

filename_set=[]
file_list="output.txt"
input_file = open(file_list,"r")
next(input_file)
for line in input_file:
    line=line.strip()
    filename_set.append("line")
input_file.close()
for filename in filename_set:
    samples=[]
    output_file=[]
    id_flag=0
    sample_flag=0
    #filename="D:/1000_data/ALL.chrY.phase3_integrated_v2a.20130502.genotypes.vcf"
#    filename="D:/1000_data/ALL.chr22.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf"
    input_file = open(filename,"r")
    for line in input_file:
        line=line.strip()
        if "POS" in line and "FORMAT" in line:
            node=line.split('\t')
            for i in range(len(node)):
                if node[i]=="ID":
                    id_flag=i
                if node[i]=="FORMAT":
                    sample_flag=i+1
                elif sample_flag!=0:
                    samples.append(node[i])
        elif id_flag!=0:
            node=line.split('\t')
            SNP_NAME=node[id_flag]
            if SNP_NAME!=".": ##check line data by ID is . or not
                if SNP_NAME in SNP_score:
                    original_sample_score=node[sample_flag:]
                    sample_score=["" for i in range(len(original_sample_score))]
                    for i in range(len(original_sample_score)):
                        temp_sum=original_sample_score[i].split('|')
                        temp_sum=[int(s) for s in temp_sum]
                        sample_score[i]=sum(temp_sum)
                    sample_score=[i * SNP_score[SNP_NAME] for i in sample_score]
                    sample_score=[str(s) for s in sample_score]
                    sample_name='\t'.join(sample_score)
                    output_file.append(node[id_flag]+'\t'+sample_name+'\n')
            
    f = open(filename.split(".")[1]+'_fit_GWAS_result.txt','w')
    f.write("SNPS\t")
    for sample in samples:
        f.write(sample+"\t")
    f.write("\n")
    for i in range(len(output_file)):
        f.write(output_file[i])
    f.close()     
                
    sample_score=["" for i in range(len(original_sample_score))]
    for i in range(len(original_sample_score)):
        temp_sum=original_sample_score[i].split('|')
        temp_sum=[int(s) for s in temp_sum]
        sample_score[i]=sum(temp_sum)
