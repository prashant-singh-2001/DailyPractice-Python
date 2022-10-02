# def update_marks(x):
#     print(x, "UPDATE")


# update_marks("Khushi")

# f = update_marks

# f("Prashant")

# del update_marks


# def update_marks():
#     print("New Update")

# update_marks()

# f("XI")

# def canteen_free_kardi_jaye(x):
#     x = x-5000
#     return x


# def fees_hata_di_jaye(x):
#     x = x+5000
#     return x


# def performance(func, x):
#     z = func(x)
#     return z


# d = performance(fees_hata_di_jaye, 50000)

# e = performance(canteen_free_kardi_jaye, 50000)

# print(d)

# print(e)

# def show():
#     print("in show")
#     return 1000

# def s():
#     print("in deis")
#     return 111

# def vision(fun):
#     print(fun)


# vision(show())
# vision(s())

class ANIMAL:

    arms = ""

    legs = ""

    def __init__(self):
        self.arms = 2
        self.legs = 4
        print(self.arms, self.legs)

    def set(self, a, b):
        self.arms = a
        self.legs = b

    def show(self):
        print(self.legs, self.arms)

dheeraj = ANIMAL()

dheeraj.set(4, 5)

dheeraj.show()
