str1 = input("Enter your first string: ")
str2 = input("Enter your second string: ")


class String:
    def __init__(self,str1,str2):
        self.str1 = str1
        self.str2 = str2
        self.longes_str = ""

    def string(self):
        for i in range(len(self.str1)):
            for j in range(i, len(self.str1)):
                sub_str = self.str1[i:j+1]
                if sub_str in self.str2:
                    if len(sub_str) > len(self.longes_str):
                        self.longes_str = sub_str
        return self.longes_str
S = String(str1,str2)
print(S.string())
