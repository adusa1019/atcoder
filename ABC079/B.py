def solve(string):
    lucas = [2, 1]
    for i in range(2, 87):
        lucas.append(sum(lucas[-2:]))
    return str(lucas[int(string)])


if __name__ == '__main__':
    print(solve(input()))
