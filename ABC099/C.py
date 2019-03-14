from math import ceil, log


def solve(string):
    n = int(string)
    max_number = 10**5
    can_operate = [1] + [6**(i + 1) for i in range(ceil(log(max_number, 6)))
                        ] + [9**(i + 1) for i in range(ceil(log(max_number, 9)))]
    can_operate = sorted(can_operate)
    dp = [0]
    for _ in range(n):
        count = n
        for o in can_operate:
            index = len(dp) - o
            if index < 0:
                break
            count = min(count, dp[index] + 1)
        dp.append(count)
    return str(dp[-1])


if __name__ == '__main__':
    print(solve(input()))
