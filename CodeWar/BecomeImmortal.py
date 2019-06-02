def recursion(m, n, l, t):
    print(m, n)
    if m * n == 0:
        return 0
    i = 0
    while 2 ** i < m or 2 ** i < n:
        i += 1
    x = 2 ** i
    print(x)
    ret = ((x - l) * (x - l - 1) * (m + n - x) // 2 + recursion(x - m, x - n, l, t)) % t
    return ret

ans = recursion(800, 500, 12, 100)
print(ans)
