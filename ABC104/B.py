def solve(string):
    is_a = string[0] == "A"
    index_c = string.find("C")
    rest = string[1:index_c] + string[index_c + 1:]
    return "AC" if is_a and 1 < index_c < len(string) -1 and rest == rest.lower() else "WA"


if __name__ == '__main__':
    print(solve(input()))
