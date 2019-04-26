# coding=utf-8
"""
create on : 2019/04/17
project name : AtCoder
file name : 07_ABC085B

Problem : https://atcoder.jp/contests/abs/tasks/abc085_b

"""


def main():
    n = int(input())
    d_list = []
    for _ in range(n):
        d_list.append(int(input()))

    stack_count = len(set(d_list))
    print(stack_count)


if __name__ == "__main__":
    main()
