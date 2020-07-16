import re


def main():
    handle = open('regex_sum_686640.txt')
    sumn = 0
    for lines in handle:
        print(lines)
        a = re.findall('[0-9]+',lines)
        s = 0
        for elm in a:
            s = s + int(elm)
        sumn = sumn + s

    print(sumn)


if __name__ == "__main__":
    main()
