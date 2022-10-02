
a = []
i = 1
while i < 4 and i > 0:
    print("----------------------------------------")
    print("queue mai jodne ki liye 1 dabaye")
    print("queue se hatane ki liye 2 dabaye")
    print("queue dikhane ke liye 3 dabaye")
    print("Bahar nikalne ke liye 4 dabaye")
    i = int(input("Ank dababye : "))
    print("-----------------------------------------")
    if i == 1:
        a.append(int(input("\n Anko ki shrankhala dijiye : ")))
    if i == 2:
        if len(a) != 0:
            a.remove(a[0])
        else:
            print("Phle push to karo!")
    if i == 3:
        print("\n", a)
