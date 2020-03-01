# MIXCR:
# Parser for extracting cdr3 seq, count and frequency from MIXCR output and converting to csv with sample name.

ls raw_data/complete_sample/MIXCR_Data/*_clones.txt | cut -d "/" -f4 | awk -F "_clones.txt" '{print $1}' > MIXCR_samples.txt

while read line
do
python scripts/mixcr.extract.py raw_data/complete_sample/MIXCR_Data/${line}_clones.txt raw_data/complete_sample/MIXCR_Data/extracted_features/${line}.extracted_MIXCR.csv
done<MIXCR_samples.txt

# python /Users/aaronkarlsberg/Desktop/TCR.Seq.Compare/scripts/mixcr.extract.py /Users/aaronkarlsberg/Desktop/TCR.Seq.Compare/raw_data/complete_sample/MIXCR_Data/${file_name} /Users/aaronkarlsberg/Desktop/TCR.Seq.Compare/raw_data/complete_sample/MIXCR_Data/extracted_features/${file_name}.parsed













