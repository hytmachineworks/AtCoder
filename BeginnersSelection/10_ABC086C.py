# coding=utf-8
"""
create on : 2019/04/19
project name : AtCoder
file name : 10_ABC086C 

Problem : https://atcoder.jp/contests/abs/tasks/arc089_a

"""


def main():
    n = int(input())

    last_time = 0
    last_x = last_y = 0

    flag = True

    for _ in range(n):
        t, x, y = [int(txy) for txy in input().split(" ")]

        dt = t - last_time

        dx = abs(x - last_x)
        dy = abs(y - last_y)

        d_dist = dx + dy

        if (dt - d_dist) >= 0 and (dt - d_dist) % 2 == 0:
            pass

        else:
            flag = False

    if flag:
        print("Yes")

    else:
        print("No")


if __name__ == "__main__":
    main()
