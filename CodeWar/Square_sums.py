def function(n):
    squares = [x ** 2 for x in range(1, n + 1) if x ** 2 < 2 * n]
    dic = {}
    for num in range(1, n + 1):
        dic[num] = [x - num for x in squares if 0 < x - num <= n and x != 2 * num]
    start_end = [num for num in dic if len(dic[num]) == 1]
    return None if len(start_end) != 2 else findPath(n, dic, *start_end)

def findPath(n, dic, start, end):
    paths = [[start]]
    while end not in [path[-1] for path in paths] and paths:
        temp = []
        for path in paths:
            for nex in dic[path[-1]]:
                if nex in path or (nex == end and len(path) != n - 1):
                    continue
                temp.append(path + [nex])
        paths = temp
    for path in paths:
        if len(path) == n and path[-1] == end:
            return path
    return None

if __name__ == '__main__':
    for n in range(15, 1000):
        ret = function(n)
        if ret:
            print(n, ret)
