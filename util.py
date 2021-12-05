def read_input(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.replace('\n',''))
    return data