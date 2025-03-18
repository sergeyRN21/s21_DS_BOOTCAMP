#!/bin/sh

input_file="../ex03/hh_position.csv"

cat "$input_file" | tail -n +2 | cut -d ',' -f 3 | sort | uniq -c | sort -rn > hh_uniq_positions.csv

sed -i '1i\"name\",\"count\"' hh_uniq_positions.csv