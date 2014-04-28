class A:
    def __init__(self):
        self.x = 3


    def f(self, y):
        return self.x + y


# python 2 -> unbound error
#print A.f(2)

# python 3
#print(A.f(2))
# takes two arguments

class A_mock:
    def __init__(self):
        self.x = 2

        
print(A.f(A_mock(), 2))
