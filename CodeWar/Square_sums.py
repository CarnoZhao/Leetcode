def function(n):
    squares = [x ** 2 for x in range(1, n + 1) if x ** 2 < 2 * n]
    dic = {}
    for num in range(1, n + 1):
        dic[num] = [x - num for x in squares if 0 < x - num <= n and x != 2 * num]
    print(dic)

if __name__ == '__main__':
    for n in range(20, 35):
        ret = function(n)
        if ret:
            print(n, ret)
