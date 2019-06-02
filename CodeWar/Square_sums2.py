def square_sums(n):
    squares = [x ** 2 for x in range(1, n + 1) if x ** 2 < 2 * n]
    dic = dict((num, [x - num for x in squares if 0 < x - num <= n and x != 2 * num]) for num in range(1, n + 1))
    degrees = [len(dic[num]) for num in range(1, n + 1)]
    start = degrees.index(min(degrees)) + 1
    for num in dic[start]:
        degrees[num - 1] -= 1
    path = dfs_extend(dic, [start], n, degrees)
    return path if len(path) == n else False

def dfs_extend(dic, path, n, degrees):
    choices = set(dic[path[-1]]) - set(path)
    try:
        mindgr = min(degrees[num - 1] for num in choices)
    except:
        return path
    for nex in choices:
        if degrees[nex - 1] == mindgr:
            for num in dic[nex]:
                degrees[num - 1] -= 1
            ret = dfs_extend(dic, path + [nex], n, degrees)
            for num in dic[nex]:
                degrees[num - 1] += 1
            if ret and len(ret) == n:
                return ret
    
if __name__ == '__main__':
    n = 997
    # path = function(n)
    path = square_sums(n)
    print(n, len(path) == n)
