touch rows.txt
echo "NUMBER OF DATA ROWS : " >> rows.txt
echo "                      " >> rows.txt

wc -l permits.csv >> rows.txt
cat rows.txt


echo "                      " >> rows.txt
echo "                      " >> rows.txt
echo "                      " >> rows.txt



echo "ALL ENTRIES WITH THE STRING 'Hyde Park' :" >> rows.txt
echo "                      " >> rows.txt
grep "Hyde Park" permits.csv >> rows.txt 

grep "Hyde Park" permits.csv >> permits_hydepark.csv


open rows.txt
open permits_hydepark.csv

