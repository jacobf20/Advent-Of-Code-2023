adjacent_symbols = {}
valid_gears = []
def check_validity(data, i, j):
    if i == 0 and j == 0:
        add_adjacency(data[i+1][j], i+1, j)
        add_adjacency(data[i][j+1], i, j+1)
        add_adjacency(data[i+1][j+1], i+1, j+1)
        return is_special(data[i + 1][j]) or is_special(data[i][j + 1]) or is_special(data[i + 1][j + 1])
    elif i == 0 and j < len(data[0]) - 1:
        add_adjacency(data[i+1][j-1], i+1, j-1)
        add_adjacency(data[i+1][j], i+1, j)
        add_adjacency(data[i+1][j+1], i+1, j+1)
        add_adjacency(data[i][j-1], i, j-1)
        add_adjacency(data[i][j+1], i, j+1)
        return is_special(data[i + 1][j - 1]) or is_special(data[i + 1][j]) or is_special(data[i + 1][j + 1]) \
            or is_special(data[i][j - 1]) or is_special(data[i][j + 1])
    elif j == 0 and i < len(data) - 1:
        add_adjacency(data[i+1][j], i+1, j)
        add_adjacency(data[i+1][j+1], i+1, j+1)
        add_adjacency(data[i][j+1], i, j+1)
        add_adjacency(data[i-1][j], i-1, j)
        add_adjacency(data[i-1][j+1], i-1, j+1)
        return is_special(data[i + 1][j]) or is_special(data[i + 1][j + 1]) or is_special(data[i][j + 1]) \
            or is_special(data[i - 1][j]) or is_special(data[i - 1][j + 1])
    elif i == len(data) - 1 and j == len(data[0]) - 1:
        add_adjacency(data[i-1][j], i-1, j)
        add_adjacency(data[i][j-1], i, j-1)
        add_adjacency(data[i-1][j-1], i-1, j-1)
        return is_special(data[i - 1][j]) or is_special(data[i][j - 1]) or is_special(data[i - 1][j - 1])
    elif i == len(data) - 1:
        add_adjacency(data[i-1][j], i-1, j)
        add_adjacency(data[i][j-1], i, j-1)
        add_adjacency(data[i-1][j-1], i-1, j-1)
        add_adjacency(data[i][j+1], i, j+1)
        add_adjacency(data[i-1][j+1], i-1, j+1)
        return is_special(data[i - 1][j]) or is_special(data[i][j - 1]) or is_special(data[i - 1][j - 1]) \
            or is_special(data[i][j + 1]) or is_special(data[i - 1][j + 1])
    elif j == len(data[0]) - 1:
        add_adjacency(data[i-1][j], i-1, j)
        add_adjacency(data[i][j-1], i, j-1)
        add_adjacency(data[i-1][j-1], i-1, j-1)
        add_adjacency(data[i+1][j], i+1, j)
        add_adjacency(data[i+1][j-1], i+1, j-1)
        return is_special(data[i - 1][j]) or is_special(data[i][j - 1]) or is_special(data[i - 1][j - 1]) \
            or is_special(data[i + 1][j]) or is_special(data[i + 1][j - 1])
    else:
        add_adjacency(data[i-1][j-1], i-1, j-1)
        add_adjacency(data[i-1][j], i-1, j)
        add_adjacency(data[i-1][j+1], i-1, j+1)
        add_adjacency(data[i][j-1], i, j-1)
        add_adjacency(data[i][j+1], i, j+1)
        add_adjacency(data[i+1][j-1], i+1, j-1)
        add_adjacency(data[i+1][j], i+1, j)
        add_adjacency(data[i+1][j+1], i+1, j+1)
        return is_special(data[i - 1][j - 1]) or is_special(data[i - 1][j]) or is_special(data[i - 1][j + 1]) \
            or is_special(data[i][j - 1]) or is_special(data[i][j + 1]) or is_special(data[i + 1][j - 1]) \
            or is_special(data[i + 1][j]) or is_special(data[i + 1][j + 1])


def find_valid_gears(data):
    for i in range(len(data)):
        row = data[i]
        for j in range(len(row)):
            if row[j] == "*":
                adjacent = []
                if i == 0 and j == 0:
                    adjacent.append(data[i][j+1])
                    adjacent.append(".")
                    adjacent.append(data[i+1][j]), adjacent.append(data[i+1][j+1])
                elif i == 0 and j < len(data[0]) - 1:
                    adjacent.append(data[i][j - 1]), adjacent.append("."), adjacent.append(data[i][j+1])
                    adjacent.append(".")
                    adjacent.append(data[i+1][j-1]), adjacent.append(data[i+1][j]), adjacent.append(data[i+1][j+1])
                elif j == 0 and i < len(data) - 1:
                    adjacent.append(data[i - 1][j]), adjacent.append(data[i-1][j+1])
                    adjacent.append(".")
                    adjacent.append(data[i][j + 1])
                    adjacent.append(".")
                    adjacent.append(data[i+1][j]), adjacent.append(data[i+1][j+1])
                elif i == len(data) -1 and j == len(data[0]) - 1:
                    adjacent.append(data[i-1][j-1]), adjacent.append(data[i-1][j])
                    adjacent.append(".")
                    adjacent.append(data[i][j-1])
                elif i == len(data) - 1:
                    adjacent.append(data[i-1][j-1]), adjacent.append(data[i-1][j]), adjacent.append(data[i-1][j+1])
                    adjacent.append(".")
                    adjacent.append(data[i][j-1]), adjacent.append("."), adjacent.append(data[i][j+1])
                elif j == len(data[0]) - 1:
                    adjacent.append(data[i-1][j-1]), adjacent.append(data[i-1][j])
                    adjacent.append(".")
                    adjacent.append(data[i][j-1])
                    adjacent.append(".")
                    adjacent.append(data[i+1][j-1]), adjacent.append(data[i+1][j])
                else:
                    adjacent.append(data[i-1][j-1]), adjacent.append(data[i-1][j]), adjacent.append(data[i-1][j+1])
                    adjacent.append(".")
                    adjacent.append(data[i][j-1]), adjacent.append("."), adjacent.append(data[i][j+1])
                    adjacent.append(".")
                    adjacent.append(data[i+1][j-1]), adjacent.append(data[i+1][j]), adjacent.append(data[i+1][j+1])

                count = 0
                num = False
                for adj in adjacent:
                    if adj.isdigit() and not num:
                        count += 1
                        num = True
                    elif adj == ".":
                        num = False

                if count == 2:
                    valid_gears.append((i,j))


def is_special(c):
    return not c.isdigit() and not c == "."


def add_adjacency(c, i, j):
    global adjacent_symbols
    if not c in adjacent_symbols.keys():
        adjacent_symbols[c] = [(i,j)]
    elif (i,j) not in adjacent_symbols[c]:
        adjacent_symbols[c].append((i,j))


def main():
    with open("input3.txt") as f:
        lines = f.readlines()
        data = [list(line.strip()) for line in lines]
        find_valid_gears(data)
        nums = []
        gear_ratios = {}
        for i in range(len(data)):
            row = data[i]
            valid_num = False
            possible_num = ""
            global adjacent_symbols
            adjacent_symbols = {}
            for j in range(len(row)):
                if row[j].isdigit():
                    if check_validity(data, i, j):
                        valid_num = True
                    possible_num += row[j]
                if (not row[j].isdigit()) and len(possible_num) > 0:
                    if "*" in adjacent_symbols.keys():
                        for coord in adjacent_symbols["*"]:
                            if coord in valid_gears:
                                if coord not in gear_ratios.keys():
                                    gear_ratios[coord] = int(possible_num)
                                else:
                                    gear_ratios[coord] = gear_ratios[coord] * int(possible_num)
                    if valid_num:
                        nums.append(int(possible_num))
                    valid_num = False
                    possible_num = ""
                    adjacent_symbols = {}
            if len(possible_num) > 0 and valid_num:
                if "*" in adjacent_symbols.keys():
                    for coord in adjacent_symbols["*"]:
                        if coord in valid_gears:
                            if coord not in gear_ratios.keys():
                                gear_ratios[coord] = int(possible_num)
                            else:
                                gear_ratios[coord] = gear_ratios[coord] * int(possible_num)
                nums.append(int(possible_num))

        print(sum(gear_ratios.values()))
        print(sum(nums))


main()
