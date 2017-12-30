import os
import re
import numpy as np

disease=[]
SNPS=[]
p_value=[]
mlog_p_value=[]
beta=[]

#retval = os.getcwd()
filename="gwas_rawdata_filter_col.txt"
input_file = open(filename,"r")
next(input_file)
for line in input_file:
    node=line.split("\t")
    disease.append(str(node[0]))
    SNPS.append(str(node[1]))
    p_value.append(float(node[2]))
    mlog_p_value.append(float(node[3]))
    if(node[4]=="\n"):
        beta.append("")
    else:
        beta.append(float(node[4].split("\n")[0]))
input_file.close()

range_sum=[0 for i in range(500)]
range_count=[0 for i in range(500)]
range_average=[0 for i in range(500)]

for i in range(len(p_value)):
    range_sum[int(mlog_p_value[i])]+=mlog_p_value[i]
    range_count[int(mlog_p_value[i])]+=1
for i in range(len(range_count)):
    if range_count[i]!=0:
        range_average[i]=float(range_sum[i]/range_count[i])

for j in range(len(beta)):
    if beta[j]=="":
        access_value=int(mlog_p_value[j])
        beta[j]=range_average[access_value]
        
f = open('acess_beta.txt','w')
f.write("DISEASE/TRAIT\tSNPS\tP-VALUE\tPVALUE_MLOG\tOR or BETA\n")
for i in range(len(disease)):
    f.write(str(disease[i])+'\t'+str(SNPS[i])+'\t'+str(p_value[i])+'\t'+str(mlog_p_value[i])+'\t'+str(beta[i])+'\n')
f.close()      
# =============================================================================
# check beta still have empty value or not!
# for i in range(len(beta)):
#     if beta=="":
#         print("still emptttttty")
# print("Done!")
# =============================================================================
# =============================================================================
# read all file in floder
# from os import listdir
# from os.path import isfile, isdir, join
# mypath = os.getcwd()
# files = listdir(mypath)
# 
# # 以迴圈處理
# for f in files:
#   # 產生檔案的絕對路徑
#   fullpath = join(mypath, f)
#   # 判斷 fullpath 是檔案還是目錄
#   if isfile(fullpath):
#     print("檔案：", f)
#   elif isdir(fullpath):
#     print("目錄：", f)
# =============================================================================
