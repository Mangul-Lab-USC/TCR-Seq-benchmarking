# TRUST:
# Parser for extracting cdr3 seq, count and frequency from TRUST output and converting to csv with sample name.
ls raw_data/complete_sample/TRUST4_Data/*.fastq.sort._report.tsv | cut -d "/" -f4 | awk -F ".fastq.sort._report.tsv" '{print $1}' >TRUST_samples.txt

while read line
do
	python scripts/TRUST4.extract.py raw_data/complete_sample/TRUST4_Data/${line}.fastq.sort._report.tsv raw_data/complete_sample/TRUST4_Data/extracted_features/${line}.extracted_TRUST4.csv
done<TRUST_samples.txt

# python /Users/aaronkarlsberg/Desktop/TCR.Seq.Compare/scripts/TRUST4.extract.py /Users/aaronkarlsberg/Desktop/TCR.Seq.Compare/raw_data/complete_sample/TRUST4_Data/${filename} /Users/aaronkarlsberg/Desktop/TCR.Seq.Compare/raw_data/complete_sample/TRUST4_Data/extracted_features/${file_name}.parsed


echo "Sample,CDR3,nReads" > summary_data/complete_sample/TRUST4_merged_extracted_features.csv
tail -n +2 -q *.csv >> summary_data/complete_sample/TRUST4_merged_extracted_features.csv




