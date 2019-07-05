def solve(string):
    a, b = map(int, [string[:2], string[2:]])
    a_is_mm = True if 1 <= a <= 12 else False
    b_is_mm = True if 1 <= b <= 12 else False
    if a_is_mm and b_is_mm:
        return "AMBIGUOUS"
    if a_is_mm:
        return "MMYY"
    if b_is_mm:
        return "YYMM"
    return "NA"


if __name__ == '__main__':
    print(solve(input()))
