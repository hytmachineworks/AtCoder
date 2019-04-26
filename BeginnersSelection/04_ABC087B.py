# coding=utf-8
"""
create on : 2019/04/15
project name : AtCoder
file name : 04_ABC087B

Problem : https://atcoder.jp/contests/abs/tasks/abc087_b

"""
from itertools import combinations_with_replacement


def main():
    a_val = int(input())  # 500円 => 10
    b_val = int(input())  # 100円 => 2
    c_val = int(input())  # 50円  => 1
    x_val = int(input())  # total

    comb_count = 0

    a_list = [(500, a) for a in range(a_val+1)]
    b_list = [(100, b) for b in range(b_val+1)]
    c_list = [(50, c) for c in range(c_val+1)]

    abc_list = a_list + b_list + c_list

    for a_pow, b_pow, c_pow in combinations_with_replacement(abc_list, 3):

        dup_list = [a_pow[0], b_pow[0], c_pow[0]]

        if len(set(dup_list)) != 3:
            continue

        buf = a_pow[0] * a_pow[1] + b_pow[0] * b_pow[1] + c_pow[0] * c_pow[1]

        if x_val == buf:
            comb_count += 1

    print(comb_count)


if __name__ == "__main__":
    main()
