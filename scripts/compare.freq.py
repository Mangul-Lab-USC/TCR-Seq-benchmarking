import csv
import argparse

#---------------
#main

ap = argparse.ArgumentParser()
ap.add_argument('inFile1', help='output of ImRep')
ap.add_argument('inFile2', help='directory to save the summary of the immune repertoire')
ap.add_argument('out', help='out')

args = ap.parse_args()



dict_tcr_seq1=dict()
tcrseqSet1=set()
sum1=0


#CDR3,nReads
#CASSLGDYNEKLFF,147

file=open(args.inFile1)
reader=csv.reader(file)
next(reader,None)

for line in reader:
    cdr3=line[0]
    count=int(line[1])
    dict_tcr_seq1[cdr3]=count
    tcrseqSet1.add(cdr3)
    sum1+=count

file.close()


dict_tcr_seq2=dict()
tcrseqSet2=set()
sum2=0

file=open(args.inFile2)
reader=csv.reader(file)
next(reader,None)

for line in reader:
    cdr3=line[0]
    count=int(line[1])
    dict_tcr_seq2[cdr3]=count
    tcrseqSet2.add(cdr3)
    sum2+=count

file.close()




common_cdr3=tcrseqSet1.intersection(tcrseqSet2)

file=open(args.out,"w")
file.write("cdr3,freq1,freq2,flag\n")

for s in common_cdr3:
    freq1=dict_tcr_seq1[s]/sum1
    freq2=dict_tcr_seq2[s]/sum2
    if freq1>freq2:
        file.write(s+","+str(freq1)+","+str(freq2)+",A")
        file.write("\n")
    elif freq1==freq2:
        file.write(s + "," + str(freq1) + "," + str(freq2) + ",B")
        file.write("\n")
    else:
        file.write(s + "," + str(freq1) + "," + str(freq2) + ",C")
        file.write("\n")