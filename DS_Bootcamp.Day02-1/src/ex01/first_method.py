class Research:
    def __init__(self, filename): 
        self.filename = filename

    def file_reader(self):
        with open(self.filename, 'r') as file:
            return file.read()

if __name__ == "__main__":
    reader = Research('data.csv')
    content = reader.file_reader()
    print(content)