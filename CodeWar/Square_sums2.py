def square_sums(n):
    squares = [x ** 2 for x in range(1, n + 1) if x ** 2 < 2 * n]
    dic = dict((num, [x - num for x in squares if 0 < x - num <= n and x != 2 * num]) for num in range(1, n + 1))
    degrees = dict((num, len(dic[num])) for num in range(1, n + 1))
    mindgr = min(degrees.values())
    for num in degrees:
        if degrees[num] == mindgr:
            start = num
            break
    for num in dic[start]:
        degrees[num] -= 1
    path = dfs_extend(dic, [start], n, degrees)
    return path if len(path) == n else False

def dfs_extend(dic, path, n, degrees):
    try:
        mindgr = min(degrees[num] for num in dic[path[-1]] if num not in path)
    except:
        return path
    for nex in dic[path[-1]]:
        if nex not in path and degrees[nex] == mindgr:
            for num in dic[nex]:
                degrees[num] -= 1
            ret = dfs_extend(dic, path + [nex], n, degrees)
            for num in dic[nex]:
                degrees[num] += 1
            if ret and len(ret) == n:
                return ret
    
if __name__ == '__main__':
    n = 900
    # path = function(n)
    path = square_sums(n)
    print(n, len(path) == n)
