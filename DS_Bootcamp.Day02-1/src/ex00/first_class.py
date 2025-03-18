class Must_read:
    def __init__(self, filename): 
        self.filename = filename

    def file_reader(self):
        with open(self.filename, 'r') as file:
            print(file.read())

if __name__ == "__main__":
    reader = Must_read('data.csv')
    content = reader.file_reader()