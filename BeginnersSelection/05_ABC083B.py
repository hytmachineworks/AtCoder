# coding=utf-8
"""
create on : 2019/04/17
project name : AtCoder
file name : 05_ABC083B

Problem : https://atcoder.jp/contests/abs/tasks/abc083_b

"""


def main():

    def calc(x):
        return sum([int(x_item) for x_item in str(x)])

    n, a, b = input().split(" ")

    a_num = int(a)
    b_num = int(b)

    n_sum = sum([n_num for n_num in range(1, int(n)+1, 1)
                 if a_num <= calc(n_num) <= b_num])

    print(n_sum)


if __name__ == "__main__":
    main()
