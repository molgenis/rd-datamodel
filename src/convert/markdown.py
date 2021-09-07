

class Markdown():
    
    # @name __init__
    # @description create a new instance and create file
    # @param file path to file location
    def __init__(self, file: str = None):
        self.file = file
        self.md = self.new_md(self.file)
        
    # @name __linebreaks__
    # @description insert n number of line breaks
    def __write__linebreaks__(self, n: int = 2):
        self.md.write('\n' * n)
    
    # @name new_md
    # @description Create a stream to a markdown file
    # @param file filepath to markdown file
    def new_md(self, file):
        return open(file, mode = 'w', encoding = 'utf-8')

    
    # @name write_header
    # @description Write a markdown header (1 through 6)
    # @param
    def write_header(self, level: int = 1, title: str = ''):
        if not level >= 1 and not level <= 6:
            raise ValueError('Error in write_header: level must be between 1 - 6')
        self.md.write('#' * level + ' ', title)
        self.__write__linebreaks__()

    # @name write
    # @description write markdown text
    # @param text content to write to file
    def write(self, *text):
        self.md.write(' '.join(map(str, text)))
        self.__write__linebreaks__()
        