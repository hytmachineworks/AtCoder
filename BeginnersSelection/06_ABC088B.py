# coding=utf-8
"""
create on : 2019/04/17
project name : AtCoder
file name : 06_ABC088B

Problem : https://atcoder.jp/contests/abs/tasks/abc088_b

"""


def main():
    n = int(input())
    a_list = sorted([int(item) for item in input().split(" ")], reverse=True)

    alice_bob = [0, 0]

    for i in range(n):
        alice_bob[i % 2] += a_list[i]

    print(alice_bob[0] - alice_bob[1])


if __name__ == "__main__":
    main()
