# python /Users/aaronkarlsberg/Desktop/TCR.Seq.Compare/scripts/mixcr.extract.py /Users/aaronkarlsberg/Desktop/TCR.Seq.Compare/raw_data/complete_sample/MIXCR_Data/CMT-baseline1C_CAGATC_combinedLanes_clones.txt /Users/aaronkarlsberg/Desktop/TCR.Seq.Compare/raw_data/complete_sample/MIXCR_Data/extracted_features/CMT-baseline1C_CAGATC_combinedLanes_clones.txt.parsed
import csv
import argparse
from math import log as ln
import sys


def p(n, N):
    """ Relative abundance """
    if n is  0:
        return 0
    else:
        return (float(n)/N) * ln(float(n)/N)

def sdi(data):
    N = sum(data.values())

    return -sum(p(n, N) for n in data.values() if n is not 0)

#============================
ap = argparse.ArgumentParser()
ap.add_argument('input', help='<Mixcr_clones.txt>')
ap.add_argument('out_prefix', help='name of outfile and save location')
args = ap.parse_args()

#0       165826  0.5418123362238529      TGTGCTGTGAGGCCCCTGTACGGAGGAAGCTACATACCTACATTT   NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN   TRAV21*00(626.1)                TRAJ6*00(262.2) TRAC*00(226.8)  324|338|356|0|14||70.0          27|51|82|21|45||120.0                                                                                           TGTGCTGTGAGGCCCCTGTACGGAGGAAGCTACATACCTACATTT   45                                                              CAVRPLYGGSYIPTF         :::::::::0:2:14:::::21:-7:45:::

set_cdr3=set()
dict={}

#get all CDR3s
file=open(args.input)
reader=csv.reader(file)
next(reader,None)
for line in reader:
    cdr3=line[0]
    if cdr3[0] == "C" and cdr3[len(cdr3) - 1] == "F":
        set_cdr3.add(cdr3)
file.close()



for c in set_cdr3:
    dict[c]=0

#get number of reads

file=open(args.input)
reader=csv.reader(file)
next(reader,None)
for line in reader:
    nReads=int(line[1])
    cdr3=line[0]
    if cdr3[0]=="C" and cdr3[len(cdr3)-1]=="F":
        dict[cdr3]+=nReads
    else:
        print (cdr3)

file.close()


print ("Nummber CDR3s",len(set_cdr3))

total_reads=float(sum(dict.values()))



fileOut=open(args.out_prefix+".cdr3.csv","w")
fileOut.write("Sample,CDR3,nReads")
fileOut.write("\n")

sample_name = args.input.split("/")[-1].split(".")[0]

for key, value in dict.items():
    fileOut.write(sample_name+","+key+","+str(value)+","+str(value/total_reads))
    fileOut.write("\n")


fileOut.close()

# alpha diversity
# fileOut=open(args.out_prefix+".alpha.diversity.csv","w")
# fileOut.write(args.out_prefix+","+str(sdi(dict)))
# fileOut.write("\n")



