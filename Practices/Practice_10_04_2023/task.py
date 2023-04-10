# class myClass:
#     def __init__(self, age, gender, name):
#         self.age = age
#         self.gender = gender
#         self.name = name

#     def getName(self):
#         return self.name


# object = myClass(20, 'M', "Maxim")

# print(dir(object), end='\n\n')
# print(dir(myClass), end='\n\n')

# print(vars(object), end='\n\n')
# print(vars(myClass), end='\n\n')

# print(object.__dict__, end='\n\n')
# print(myClass.__dict__, end='\n\n')

# print(getattr(object, "getName")())


# class A:
#     pass


# class B(A):
#     pass


# class C(B):
#     pass


# def get_inheritance(T):
#     return ' -> '.join([c.__name__ for c in T.mro()])


# print(get_inheritance(C))


class hashTable:
    size = 0
    filled = 0
    table = []

    def __init__(self, size):
        self.size = size
        for i in range(self.size):
            self.table.append([1, 1])

    def __setitem__(self, value):
        pass

    def __getitem__():
        pass

    def __len__():
        pass


my_table = hashTable(16)
my_table.__setitem__(3)
