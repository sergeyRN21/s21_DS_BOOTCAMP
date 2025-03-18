#!/bin/sh

input_file="../ex00/hh.json"

jq -f filter.jq $input_file > hh.csv
