import random
class Generate:
    
    def generate_password(self,length):
        char = "abcdefghjklmnopqrstuvxyzABCDEFGHJKLMNOPQRSTUVXYZ1234567890!@#$%^&*"
        num_of_char = len(char)
        password = ""
        for _ in range(length):
            rand_index = random.randrange(0,num_of_char)
            password+=char[rand_index]
        return password
password_length = 8
G = Generate()

random_password = G.generate_password(password_length)
print(random_password)



