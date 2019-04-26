# coding=utf-8
"""
create on : 2019/04/19
project name : AtCoder
file name : 08_ABC085C 

Problem : https://atcoder.jp/contests/abs/tasks/abc085_c

"""


def main():

    def return_str(k, l, m):
        print(" ".join([str(int(klm)) for klm in [k, l, m]]))

    n, y = (int(i) for i in input().split(" "))

    for a in range(n+1):

        for b in range(n+1):

            if n - (a + b) < 0:
                continue

            c = n - (a + b)
            sum_y = 10000 * a + 5000 * b + 1000 * c

            if sum_y == y:
                return return_str(a, b, c)

    a = b = c = -1
    return return_str(a, b, c)


if __name__ == "__main__":
    main()
