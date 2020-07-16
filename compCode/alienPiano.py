t = int(input())
en = 1
while t:
    count = 0
    n = int(input())
    arr = [int(i) for i in input().split()]
    ctr = 1
    ltr = 1
    for i in range(n - 1):
        print('ctr : ', ctr, 'ltr : ', ltr)
        if arr[i] < arr[i + 1] and ctr < 4:
            ctr += 1
            ltr = 1
            # if ctr > uprl: uprl = ctr
            # if lwrl > 0:
            #     lwrl = 0
            #     ctr = 2

        elif arr[i] > arr[i + 1] and ltr < 4:
            ltr = ltr + 1
            ctr = 1
            # if lwrl > ctr: lwrl = ctr
            # if uprl < 5:
            #     uprl = 5
            #     ctr = 3

        elif arr[i] == arr[i + 1]:
            print(end='')
        else:
            count += 1
            ctr = 1
            ltr = 1
    opt = 'Case #' + str(en) + ':'
    print(opt, count)
    en += 1
    t -= 1