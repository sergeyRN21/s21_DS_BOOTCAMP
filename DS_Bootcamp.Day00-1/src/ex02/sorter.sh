#!/bin/sh


INPUT_FILE="../ex01/hh.csv"

head -n 1 $INPUT_FILE > hh_sorted.csv

tail -n +2 $INPUT_FILE | sort -t ',' -k 2,2 -k 1,1 >> hh_sorted.csv