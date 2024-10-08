# task_2
# number_1

message = "###!!@mocleW EPGTQ!!!6789"
extract = message.split('@')[1].split('!')[0]
print(extract)
# number_2

reversed_message=extract[::-1].split(' ')[1]
print(reversed_message)
# number_3

vowels = "aeiouAEIOU"
the_final_word = extract.split(' ')[1]

# Remove vowels from the second word
for char in vowels:
    the_final_word = the_final_word.replace(char, "")
print(the_final_word)
# number_4    

final_decoded_message = f"{reversed_message} {the_final_word}"
print("Final decoded message:", final_decoded_message)