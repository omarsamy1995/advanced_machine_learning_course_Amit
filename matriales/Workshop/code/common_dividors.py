class Dividors:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def dividors(self):
        mn = min(self.num1, self.num2)
        common_dividors = []
        for i in range(1, mn+1):
            if self.num1 % i == 0 and self.num2 % i ==0:
                common_dividors.append(i)
        return common_dividors

D = Dividors(20,10)
print(D.dividors())
