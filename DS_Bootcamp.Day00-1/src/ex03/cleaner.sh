#/bin/sh

INPUT_FILE="../ex02/hh_sorted.csv"

OUTPUT_FILE=hh_position.csv

awk '
BEGIN {
    FS=OFS=","
    regexes["Junior"] = "[Jj]unior\\+?/?"
    regexes["Middle"] = "[Mm]iddle\\+?/?"
    regexes["Senior"] = "[Ss]enior"
}
{
    found_match = ""
    
    for (level in regexes) {
        if ($3 ~ regexes[level]) {
            found_match = level
            break
        }
    }
    
    if (found_match != "") {
        $3 = "\"" found_match "\""
    } else {
        $3 = "\"-\""
    }
    
    print
}' "$INPUT_FILE" >> "$OUTPUT_FILE"