with open("population.txt") as population:
    pop = [i.strip().split("\t") for i in population.readlines()]
    for i in pop:
        if i[0][0] == "G" and int(i[1]) > 500_000:
            print(i[0])