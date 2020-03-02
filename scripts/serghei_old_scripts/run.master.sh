#!/bin/bash


if [ $# -lt 3 ]
then


echo "[1] - TCR-SEQ file"
echo "[2] - rna seq file"
echo "[3] - prefix with dir"
exit 1
fi


DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo $DIR

python ${DIR}/compare.py $1 $2 $3
Rscript ${DIR}/compare.R $3
