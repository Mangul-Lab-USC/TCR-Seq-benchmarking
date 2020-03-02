# TCR:
# Parser for extracting cdr3 seq, count and frequency from TCR seq files and converting to csv with sample name.

ls raw_data/complete_sample/TCR_seq/*.tsv | cut -d "/" -f4 | awk -F ".tsv" '{print $1}' >TCR_samples.txt

while read line
do
python scripts/tcr.seq.extract.py raw_data/complete_sample/TCR_seq/${line}.tsv raw_data/complete_sample/TCR_seq/extracted_features/${line}.extracted_TCR.csv
done<TCR_samples.txt

# python /Users/aaronkarlsberg/Desktop/TCR.Seq.Compare/scripts/tcr.seq.extract.py /Users/aaronkarlsberg/Desktop/TCR.Seq.Compare/raw_data/complete_sample/TCR_seq/${filename} /Users/aaronkarlsberg/Desktop/TCR.Seq.Compare/raw_data/complete_sample/TCR_seq/extracted_features/${file_name}.parsed

echo "Sample,CDR3,nReads" > summary_data/complete_sample/TCR_merged_extracted_features.csv
tail -n +2 -q raw_data/complete_sample/TCR_seq/extracted_features/*.csv >> summary_data/complete_sample/TCR_merged_extracted_features.csv
