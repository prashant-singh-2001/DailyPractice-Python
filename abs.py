from abc import ABC, abstractmethod


# def GOV(function):
#     def inner():
#         print("issue: NOTICE")
#         function()
#     return inner


# def MP():
#     print("Ajj ki Chutti Hai!!!")


# ab = GOV(MP)
# ab()


# @GOV
# def AP():
#     print("Collect Less TAX")


# ad = AP
# ad()


# def Prsahant(fun):
#     def inner():
#         print("Called Prashant")
#         print("He a dumb hoe!")
#         fun()
#     return inner


# @Prsahant
# def CODE():
#     print("But in code- HE A GOD!")


# ab = CODE
# ab()


# class UNIVERSITY(ABC):
#     def __init__(self):
#         super().__init__()
#         print(" ")

#     @abstractmethod
#     def payFee(self):
#         print("Print fee accordingly")
#         pass

#     @abstractmethod
#     def giveExam(self):
#         print("Exam dede makkar!!!")
#         pass


# class BCA(UNIVERSITY):
#     def __init__(self, a):
#         print(a+" joined university!")

#     def payFee(self):
#         super().payFee()
#         print("Paid Fee")

#     def giveExam(self):
#         super().giveExam()
#         print("Gave EXAM")


# x = BCA()
# x.giveExam()
# x.payFee()


class CAR():
    @abstractmethod
    def engine():
        pass

    @abstractmethod
    def wheels():
        pass

    @abstractmethod
    def brakes():
        pass

    @abstractmethod
    def gears():
        pass


class BMW(CAR):
    def engine():
        print("6 Cylinder inline Engine with 24 VALVES and Bespoke ")