num_red = 12
num_green = 13
num_blue = 14

def main():
    with open("input2.txt") as f:
        valid_games = []
        powers = []

        line = f.readline()
        while line:
            line = line.strip().split(":")
            game_str = line[0]
            game_str = game_str.strip().split()
            game_id = int(game_str[1])
            info = line[1]
            info = info.split(";")
            valid = True
            max_green = 1
            max_red = 1
            max_blue = 1
            for i in info:
                i = i.strip().replace(",", "").split()
                for j in range(1, len(i), 2):
                    if i[j] == 'green':
                        green_cubes = int(i[j-1])
                        if green_cubes > max_green:
                            max_green = green_cubes
                        if green_cubes > num_green:
                            valid = False
                    elif i[j] == 'red':
                        red_cubes = int(i[j-1])
                        if red_cubes > max_red:
                            max_red = red_cubes
                        if red_cubes > num_red:
                            valid = False
                    else:
                        blue_cubes = int(i[j-1])
                        if blue_cubes > max_blue:
                            max_blue = blue_cubes
                        if blue_cubes > num_blue:
                            valid = False
            if valid:
                valid_games.append(game_id)
            powers.append(max_red*max_green*max_blue)
            line = f.readline()

        print(sum(valid_games))
        print(sum(powers))


main()
