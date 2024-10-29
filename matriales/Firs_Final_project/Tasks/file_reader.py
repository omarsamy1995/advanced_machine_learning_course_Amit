class TextFileReader:
    """A class to read a text file and analyze its content."""

    def __init__(self, file_path):
        """Initializes the TextFileReader with the path to the text file."""
        self.file_path = file_path
        self.content = ""
    
    def read_file(self):
        """Reads the file and stores its contents."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.content = file.read()
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def count_lines(self):
        """Returns the number of lines in the file."""
        return self.content.count('\n') + 1 if self.content else 0
    
    def count_words(self):
        """Returns the total number of words in the file."""
        return len(self.content.split()) if self.content else 0
    
    def count_characters(self):
        """Returns the total number of characters in the file."""
        return len(self.content)
    
    def display_content(self):
        """Prints the content of the file."""
        print(self.content)

# Testing the TextFileReader class
def main():

    file_path = input("Enter the path to the text file: ").strip()
    text_file_reader = TextFileReader(file_path)

    text_file_reader.read_file()
    
    # Check if the content was read successfully
    if text_file_reader.content:
        print(f"Number of lines: {text_file_reader.count_lines()}")
        print(f"Number of words: {text_file_reader.count_words()}")
        print(f"Number of characters: {text_file_reader.count_characters()}")
        print("\nContent of the file:")
        text_file_reader.display_content()


if __name__ == "__main__":
    main()
