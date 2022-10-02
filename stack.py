a = []
i = 1

while i < 4 and i > 0:
    print("----------------------------------------")
    print("\nEnter 1 to push in stack ")
    print("Enter 2 to pop out of the stack")
    print("Enter 3 to display stack")
    print("ENter 4 to exit the program")
    i = int(input("Enter the choice : "))
    print("-----------------------------------------")
    if i == 1:
        a.append(int(input("\n Enter number ")))
    if i == 2:
        a.pop()
    if i == 3:
        print("\n", a)
