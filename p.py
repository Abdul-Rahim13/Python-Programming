class Number:
    Multiplier = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    def mul(self):
        return self.x * self.__class__.Multiplier
    
    def sub(self):
        return self.x - self.y
    
    def value(self):
        return(self.x, self.y)
    
    def value(self, val):
        self.x, self.y = val

    def value(self):
        self.x = None
        self.y = None

num = Number(4,5)

print(f"Add: {num.add()}")
print(f"Multiply: {num.mul()}")
print(f"sub: {num.sub()}")

num.value = (1,2)
print(f"updated value: {num.value}")

del num.value
print(f"Deleted: {num.value}")

