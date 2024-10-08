# Task_4

# number_1

message = "##$$$@!yalpstcejorp EPUVT****9887"
extract = message.split('!')[1].split('*')[0]
print(extract)

reversed_message=extract[::-1].split(' ')[1]
print(reversed_message)

the_last_word = message.split(' ')[1].split('*')[0]
the_new_last_word = the_last_word.replace("E","A").replace("U","O")


final_decoded_message = f"{reversed_message} {the_new_last_word}"
print("Final decoded message:", final_decoded_message)