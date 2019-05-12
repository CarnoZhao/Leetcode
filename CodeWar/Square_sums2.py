def function(n):
    squares = [x ** 2 for x in range(1, n + 1) if x ** 2 < 2 * n]
    dic = {}
    for num in range(1, n + 1):
        dic[num] = [x - num for x in squares if 0 < x - num <= n and x != 2 * num]
        dic[num].append(0)
    dic[0] = list(range(1, n + 1))

if __name__ == '__main__':
    for n in range(1000, 1001):
        ret = function(n)
        if ret:
            print(n, ret)
