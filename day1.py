import re

conversions = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5",
               "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def main():

    with open("input1.txt") as f:
        line = f.readline()
        nums = []
        while line:
            num = ""

            matching = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine))", line)

            has_match = len(matching) > 0

            print(matching)
            print(line)
            for i in range(len(line)):
                if line[i].isdigit():
                    if has_match and line.index(matching[0]) < i:
                        num += conversions[matching[0]]
                    else:
                        num += line[i]
                    break

            for i in range(len(line) - 1, -1, -1):
                if line[i].isdigit():
                    if has_match and line.rindex(matching[-1]) > i:
                        num += conversions[matching[-1]]
                    else:
                        num += line[i]
                    break

            if len(num) == 0:
                if len(matching) > 1:
                    num += conversions[matching[0]]
                    num += conversions[matching[-1]]
                elif has_match:
                    num += conversions[matching[0]]
                    num += conversions[matching[0]]
                else:
                    num = "0"

            print(num)
            nums.append(int(num))
            line = f.readline()

        total = sum(nums)

        print (total)


main()