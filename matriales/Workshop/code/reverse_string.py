class reversing:
    def __init__(self,s):
        self.s = s
    def fun(self):
        first = self.s.split(" ")
        new_first = first[::-1]
        new_str = " ".join(new_first)
        return new_str

s = input("Enter your string: ")
R = reversing(s)
print(R.fun())