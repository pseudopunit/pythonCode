import re


def inf(x):
    y = re.findall('[a-o]+', x)
    return y


def main():
    x = input('give me a string')
    print(inf(x))


if __name__ == "__main__":
    main()
