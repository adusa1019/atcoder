def solve(string):
    return string.replace("A", "B").replace("T", "A").replace("B", "T").replace("C", "B").replace(
        "G", "C").replace("B", "G")


if __name__ == '__main__':
    print(solve(input()))
