class A:
    def __init__(self):
        print("This is init of method A")
        
    def method1(self):
        print("This is method 1")

class B(A):
    def __init__(self):
        super().__init__()
        print("This is init method of B")
    
    def method2(self):
        print("This is method 2")

# class C(B):
#     def method3(self):
#         print("This is method 3")

objA = B()
# objB = B()
# objC = C()

# objA.__init__()

# inheritance is not a question
# It is a concept that you can apply
# it is a concept that a child class inherits with the parent class


