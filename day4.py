copies = {}
def main():
    with open("input4.txt") as f:
        lines = f.readlines()
        total = 0
        for i in range(1, len(lines) + 1):
            if i not in copies.keys():
                copies[i] = 1
            line = lines[i-1]
            line = line.strip().split()
            matches = 0
            win_num = []
            for j in range(2,12):
                win_num.append(line[j])
            for j in range(13, len(line)):
                if line[j] in win_num:
                    matches += 1
            if matches > 0:
                for y in range(copies[i]):
                    for x in range(i+1, matches + i + 1):
                        if x not in copies.keys():
                            copies[x] = 2
                        else:
                            copies[x] += 1
                total += pow(2, matches - 1)

        print(sum(copies.values()))
        print(total)


main()
