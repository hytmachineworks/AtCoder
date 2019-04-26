# coding = utf-8
"""
create on : 2019/04/06
project name : AtCoder
file name : 01_ABC086A

problem : https://atcoder.jp/contests/abs/tasks/abc086_a

"""


def main():
    a, b = [int(x) for x in input().split(" ")]
    ab = a * b
    ans = "Odd" if ab % 2 else "Even"
    print(ans)


if __name__ == "__main__":
    main()
