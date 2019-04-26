# coding=utf-8
"""
create on : 2019/04/19
project name : AtCoder
file name : 09_ABC049C 

Problem : https://atcoder.jp/contests/abs/tasks/arc065_a

"""


def main():
    s = input()

    flag = False

    s_len = len(s)

    pos = 0

    while not flag:
        read_5 = s[pos: pos+5]
        read_6 = s[pos: pos+6]
        read_7 = s[pos: pos+7]

        if read_6 == "eraser":
            erase_check = s[pos+4: pos+9]
            if erase_check == "erase":
                pos += 4

            else:
                pos += 6

        elif read_5 == "erase":
            pos += 5

        elif read_7 == "dreamer":
            erase_check = s[pos+5: pos+10]

            if erase_check == "erase":
                pos += 5

            else:
                pos += 7

        elif read_5 == "dream":
            pos += 5

        else:
            print("NO")
            flag = True

        if s_len == pos:
            print("YES")
            flag = True


if __name__ == "__main__":
    main()
