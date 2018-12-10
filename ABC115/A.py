def solve(string):
    D = {
        "25": "Christmas",
        "24": "Christmas Eve",
        "23": "Christmas Eve Eve",
        "22": "Christmas Eve Eve Eve"
    }
    return D[string]


if __name__ == '__main__':
    print(solve(input()))
