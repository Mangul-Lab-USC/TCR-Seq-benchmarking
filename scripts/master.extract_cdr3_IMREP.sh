# IMREP:
# Parser for extracting cdr3 seq, count and frequency from IMREP output and converting to csv with sample name.
ls raw_data/complete_sample/IMREP_Data/*.fastq.sort.cdr3 | cut -d "/" -f4 | awk -F ".fastq.sort.cdr3" '{print $1}' >IMREP_samples.txt

while read line
do
	python scripts/imrep.extract.py raw_data/complete_sample/IMREP_Data/${line}.fastq.sort.cdr3 raw_data/complete_sample/IMREP_Data/extracted_features/${line}.extracted_IMREP.csv
done<IMREP_samples.txt

# python /Users/aaronkarlsberg/Desktop/TCR.Seq.Compare/scripts/imrep.extract.py /Users/aaronkarlsberg/Desktop/TCR.Seq.Compare/raw_data/complete_sample/IMREP_Data/${file_name} /Users/aaronkarlsberg/Desktop/TCR.Seq.Compare/raw_data/complete_sample/IMREP_Data/extracted_features/${file_name}.parsed

echo "Sample,CDR3,nReads" > summary_data/complete_sample/IMREP_merged_extracted_features.csv
tail -n +2 -q raw_data/complete_sample/IMREP_Data/extracted_features/*.csv >> summary_data/complete_sample/IMREP_merged_extracted_features.csv




# python scripts/imrep.extract.py raw_data/complete_sample/IMREP_Data/hisat2.tuned_LEK-baseline_CGATGT_combinedLanes_R1_001.fastq.sort.cdr3 raw_data/complete_sample/IMREP_Data/extracted_features/hisat2.tuned_LEK-baseline_CGATGT_combinedLanes_R1_001.extracted_IMREP.csv