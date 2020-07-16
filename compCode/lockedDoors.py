t = int(input())
en = 1
while t:
    n, q = input().split()
    n = int(n)
    q = int(q)
    d = [int(i) for i in input().split()]
    ans = ''
    for i in range(q):
        s, k = input().split()
        s = int(s)
        pos = s
        vis = []
        k = int(k)
        if s == 1:
            ans += str(k) + ' '
        elif s == n - 1:
            ans += str(n - k) + ' '
        else:
            p = s - 1
            l = s
            for i in range(k):
                #print('p : ', p, 'l : ', l, d[p], d[l])
                if d[p] < d[l]:
                    pos = p
                    if p > 0:  p -= 1
                    vis.append(p)
                elif d[p] > d[l]:
                    pos = l + 1
                    if l < s: l += 1
                    vis.append(l)
            ans += str(pos + 1) + ' '
        #print('---------------------------------')

    opt = 'Case #' + str(en) + ':'
    print(opt, ans)
    en = en + 1
    t -= 1
