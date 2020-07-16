t = int(input())
cn = 1
while t:
    count = 0
    days = int(input())
    a = [int(i) for i in input().split()]
    maxv = a[0]
    for i in range(days):
        cst = a[i]
        try:
            cst2 = a[i+1]
        except:
            cst2 = -1
        if (cst > maxv or i == 0) and (cst > cst2) :
            maxv = cst
            count += 1
    opt = 'Case #' + str(cn) + ':'
    print(opt,count)
    cn += 1
    t = t - 1
