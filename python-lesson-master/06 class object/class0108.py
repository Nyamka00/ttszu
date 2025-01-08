class Triangle:
    def __init__(self, a, b, c):
         self.a = a
         self.b = b
         self.c = c 

    def is_valid(self):
        return(self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)

test = Triangle(3, 4, 5)
print(test.is_valid())
