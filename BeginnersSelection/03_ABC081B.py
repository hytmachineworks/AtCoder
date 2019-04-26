# coding=utf-8
"""
create on : 2019/04/15
project name : AtCoder
file name : 03_ABC081B

Problem : https://atcoder.jp/contests/abs/tasks/abc081_b

"""
from math import log2


def main():
    n = int(input())
    a_list = [int(a) for a in input().split(" ")[:n]]

    loop = 2 ** int(log2(max(a_list)))

    for i in range(loop):

        a_list = [a_div / 2 for a_div in a_list if a_div % 2 == 0]

        if n != len(a_list):
            print(i)
            break


if __name__ == "__main__":
    main()
