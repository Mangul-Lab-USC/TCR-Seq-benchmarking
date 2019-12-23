import csv
import argparse



ap = argparse.ArgumentParser()
ap.add_argument('in_tcr_seq', help='Mapped reads in bam format')
ap.add_argument('in_imrep', help='Mapped reads in bam format')
ap.add_argument('out_prefix', help='Mapped reads in bam format')

args = ap.parse_args()

#CDR3,nReads
#CASSPPNSVTDEQYF,1
#CASSLSGDEQFF,1
#CASSLGQGVREQYF,1

dict_tcr_seq={}
tcrseqSet=set()

file=open(args.in_tcr_seq)
reader=csv.reader(file)
next(reader,None)



for line in reader:
    cdr3=line[0]
    count=int(line[1])
    dict_tcr_seq[cdr3]=count
    tcrseqSet.add(cdr3)

file.close()

#imrep
#CAGRRGTQETQYF,5,0.0002659433008882506

dict_imrep={}
imrepSet=set()

file=open(args.in_imrep)
reader=csv.reader(file)



for line in reader:
    cdr3=line[0]
    count=line[1]
    prc=line[2]
    dict_imrep[cdr3]=(count,prc)
    imrepSet.add(cdr3)

file.close()

intersectionSet=tcrseqSet.intersection(imrepSet)



set_only_tcrseq=tcrseqSet-imrepSet



print (len(set_only_tcrseq))

total_reads_tcrseq=sum(dict_tcr_seq.values())



#========================================================================
#save FREQ of clonotypes detected by both RNA-Seq and ImReP
fileOut=open(args.out_prefix+".correlation.common.FREQ.both.csv","w")
fileOut.write("FREQ.ImReP,FREQ.TCR-Seq")
fileOut.write("\n")

for s in intersectionSet:
     fileOut.write(str(dict_imrep[s][1])+","+str(dict_tcr_seq[s]/total_reads_tcrseq))
     fileOut.write("\n")

fileOut.close()

#========================================================================
# Updated Dec 22 2017. save counts of clonotypes detected by both RNA-Seq and ImReP
fileOut=open(args.out_prefix+".correlation.common.COUNT.both.csv","w")
fileOut.write("CDR3,FREQ.ImReP,FREQ.TCR-Seq")
fileOut.write("\n")

for s in intersectionSet:
     fileOut.write(s+","+str(dict_imrep[s][0])+","+str(dict_tcr_seq[s]))
     fileOut.write("\n")

fileOut.close()


#========================================================================
# Save TCR-Seq FREQ of clonotypes captured by ImreP
fileOut=open(args.out_prefix+".FREQ.TCR.Seq.csv","w")
fileOut.write("n,FREQ.TCR.Seq,common.flag")
fileOut.write("\n")

k=0
for s in intersectionSet:
    k+=1
    fileOut.write(str(k)+","+str(dict_tcr_seq[s]/total_reads_tcrseq)+",1")
    fileOut.write("\n")


for s in set_only_tcrseq:
    k+=1
    fileOut.write(str(k)+","+str(dict_tcr_seq[s]/total_reads_tcrseq)+",0")
    fileOut.write("\n")

fileOut.close()


file=open(args.out_prefix+".FREQ.TCR.Seq.csv")


#========================================================================
# Imrep Clonotypes not confirmed by TCRB-Seq
set_only_imrep=imrepSet-tcrseqSet

fileOut=open(args.out_prefix+".RNASEQ.FREQ.csv","w")
fileOut.write("n,FREQ,count,common.flag")
fileOut.write("\n")

k=0
for s in intersectionSet:
    k+=1
    fileOut.write(str(k)+","+str(dict_imrep[s][1])+","+str(dict_imrep[s][0])+",1")
    fileOut.write("\n")


for s in set_only_imrep:
    k+=1
    fileOut.write(str(k)+","+str(dict_imrep[s][1])+","+str(dict_imrep[s][0])+",0")
    fileOut.write("\n")
fileOut.close()

#========================================================================
# Summary
print ("mixcr",len(imrepSet))
print ("tcrseq",len(tcrseqSet))
print ("common",len(intersectionSet))
ratio=len(intersectionSet)/len(imrepSet)

freq=[]
for s in set_only_tcrseq:
    freq.append(dict_tcr_seq[s]/total_reads_tcrseq)

print ("Max FREQ - missing",max(freq))
print ("Portion of repetoire mssing",sum(freq))



fileOut=open(args.out_prefix+".summary.csv","w")
fileOut.write("sample,n_tcrseq,n_rnaseq,n_common,ratio,max_missed_clonotype,prc_captured_by_rnaseq")
fileOut.write("\n")

fileOut.write(args.out_prefix+","+str(len(tcrseqSet)) +","+str(len(imrepSet))+","+str(len(intersectionSet))+","+str(ratio)+","+str(max(freq)) +","+str(sum(freq)))
fileOut.write("\n")