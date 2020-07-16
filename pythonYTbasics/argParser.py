import argparse


if __name__ == '__main__':

    # initialise the parser
    parser = argparse.ArgumentParser(description="This is the description of the module/python-script")

    # add the parameters -> positonal/optional(positional with --)
    parser.add_argument('-a', '--num1', help='provide number 1 here', type=float)
    parser.add_argument('-b', '--num2', help='provide number 2 here', type=float)
    parser.add_argument('-o', '--opr', help='provide operator ', default='+')

    # parse the arguments
    args = parser.parse_args()
    print(args)
    result = None
    if args.opr == '+':
        result = args.num1 + args.num2
    if args.opr == '-':
        result = args.num1 - args.num2
    if args.opr == '*':
        result = args.num1 * args.num2
    if args.opr == '%':
        result = args.num1 % args.num2

    print('Result :', result)
