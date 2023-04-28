with open("class_scores.txt", "r") as cs, open("new_scores.txt", "w") as ns:
    for line in cs:
        l = line.split()
        if int(l[1]) >= 95:
            print(f"{l[0]} {100}", end="\n", file=ns)
        else:
            print(f"{l[0]} {int(l[1]) + 5}", end="\n", file=ns)
