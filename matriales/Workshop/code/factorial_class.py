#make class to make a factorial
class Factorial:
    def factorial(self, num):
        if num == 0:
            return 0 
        if num == 1:
            return 1
        return num * self.factorial(num - 1)

F = Factorial()
print(F.factorial(5))
