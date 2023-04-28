
def read_csv():
    with open("data.csv") as data:
        keys = [i.strip() for i in data.readline().split(",")]
        result = []
        for line in data:
            result.append(dict(zip(keys, line.strip().split(","))))
        return result

