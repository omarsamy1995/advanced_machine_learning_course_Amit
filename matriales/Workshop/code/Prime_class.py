class Primary:
    def __init__(self,num):
        self.num = num
    def isprime(self):
        for i in range(2,self.num):
            if self.num % i == 0:
                return False
            else:
                return True
p= Primary(5)
print(p.isprime())