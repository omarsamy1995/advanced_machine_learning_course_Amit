input_file = open("D:/diploma AI/advanced_machine_learning_course_Amit/test.txt", "r")
class FileSystem:
    def __init__(self, input_file):
        self.input_file = input_file
    def file_system(self):
    
        text = self.input_file.read()
        input_file.close()
        text = text.replace('\n', ' ')
        words = text.split(' ')
        unique_words = set(words)
        word_counts = dict()

        for word in unique_words:
            word_counts[word] = words.count(word)
        output_file = open("output_file.txt", "w")
        for word in word_counts:
            output_file.write("{}: {}\n".format(word, word_counts[word]))
        output_file.close()
F = FileSystem(input_file)
print(F.file_system())