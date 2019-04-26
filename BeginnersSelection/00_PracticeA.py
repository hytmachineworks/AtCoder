# coding = utf-8
"""
create on : 2019/04/06
project name : AtCoder
file name : 00_PracticeA

problem : https://atcoder.jp/contests/abs/tasks/practice_1

"""


def main():
    a = [input()]
    bc = input().split(" ")
    s = input()
    abc = a + bc
    abc_sum = str(sum([int(num) for num in abc]))
    print("{sum} {s}".format(sum=abc_sum, s=s))


if __name__ == "__main__":
    main()
