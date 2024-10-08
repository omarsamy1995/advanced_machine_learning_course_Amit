# Task_3

# number_1

message = "&&&**$gnirtS PLIO!!@1234"
extract = message.split('$')[1].split('!')[0]
print(extract)

# number_2 
reversed_message=extract[::-1].split(' ')[1]
print(reversed_message)

#number_3

the_last_word = message.split(' ')[1].split('!')[0]
the_new_last_word = the_last_word.replace("I","E").replace("O","U")

#number_4

final_decoded_message = f"{reversed_message} {the_new_last_word}"
print("Final decoded message:", final_decoded_message)