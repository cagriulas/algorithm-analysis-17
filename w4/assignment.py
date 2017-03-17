class MyClass:
    def __init__(self):
        self.x = []

    def add(self, item):
        self.x.append(item) # O(1)

a = MyClass() # O(1)
b = MyClass()

a.add("1") b.add("2")

a = b # shallow copy, complexity O(1)

print("IDs:", "\na = ", id(a), ", b = ", id(b))
print("Is objects same: ", a is b)

a.add("3")

print("IDs:", "\na = ", id(a), ", b = ", id(b))
print("Is objects same: ", a is b)
print(a.x, b.x)

