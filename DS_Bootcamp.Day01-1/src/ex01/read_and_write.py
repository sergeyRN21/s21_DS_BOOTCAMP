def read_and_write(file_input, file_output):
    with open(file_input, 'r') as file_in:
        content = file_in.read()

    transformed_content = (
        content.replace('","', '"\t"')
               .replace('false,', 'false\t')
               .replace('true,', 'true\t')
               .replace('",', '\t')
    )

    with open(file_output, 'w') as file_out:
        file_out.write(transformed_content)

if __name__ == "__main__":
    file_input = 'ds.csv'
    file_output = 'ds.tsv'
    read_and_write(file_input, file_output)