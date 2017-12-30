import matplotlib.pyplot as plt

beta=[]
filename="acess_beta.txt"
input_file = open(filename,"r")
next(input_file)
for line in input_file:
    line=line.strip()
    node=line.split("\t")
    beta.append(float(node[4]))
input_file.close()


plt.figure()
plt.boxplot(beta, 0, '+') # change 0 ->outlier point symbols
plt.yscale('log') #y axis ->log
plt.ylim(0.33,4) # y axis limit min/max
plt.xticks([1],['BETA']) #set x label name
plt.show()