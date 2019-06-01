def bfs(n):
    squares = [x ** 2 for x in range(1, n + 1) if x ** 2 < 2 * n]
    dic = {}
    for num in range(1, n + 1):
        dic[num] = [x - num for x in squares if 0 < x - num <= n and x != 2 * num]
    mindgr = min(len(dic[num]) for num in dic)
    for num in dic:
        if len(dic[num]) == mindgr:
            start = num
            break
    paths = [[start]]
    while paths and len(paths[0]) != n:
        temp = []
        for path in paths:
            for new in dic[path[-1]]:
                if new in path:
                    continue
                temp.append(path + [new])
        paths = temp
    for path in paths:
        if path[::-1] in paths:
            paths.remove(path)
            continue
 
def extend_path_full(dic, path, start):
    while True:
        add = False
        path = extend_path(dic, path, start)
        for endnext in dic[path[-1]]:
            if endnext not in path:
                continue
            idx = path.index(endnext) + 1
            if any(out not in path for out in dic[path[idx]]):
                start = path[idx]
                path[idx:] = path[idx:][::-1]
                add = True
                break
        if not add:
            break
    return path

def extend_path(dic, path, start):
    mindgr = len(dic) + 1
    for nex in dic[start]:
        if nex in path:
            continue
        dgr = sum(x not in path for x in dic[nex])
        if dgr < mindgr:
            mindgr = dgr
            minnex = nex
    try:
        return extend_path(dic, path + [minnex], minnex)
    except:
        return path

def function(n):
    squares = [x ** 2 for x in range(1, n + 1) if x ** 2 < 2 * n]
    dic = {}
    for num in range(1, n + 1):
        dic[num] = [x - num for x in squares if 0 < x - num <= n and x != 2 * num]
    mindgr = min(len(dic[num]) for num in dic)
    for num in dic:
        if len(dic[num]) == mindgr:
            start = num
            break
    path = [start]
    path = extend_path(dic, path, start)
    return path if len(path) == n else False

def square_sums(n):
    squares = [x ** 2 for x in range(1, n + 1) if x ** 2 < 2 * n]
    dic = {}
    for num in range(1, n + 1):
        dic[num] = [x - num for x in squares if 0 < x - num <= n and x != 2 * num]
    mindgr = min(len(dic[num]) for num in dic)
    for num in dic:
        if len(dic[num]) == mindgr:
            start = num
            break
    path = dfs_extend(dic, [start], n)
    return path

def dfs_extend(dic, path, n):
    try:
        mindgr = min(sum(x not in path for x in dic[nex]) for nex in dic[path[-1]] if nex not in path)
    except:
        return path
    for nex in dic[path[-1]]:
        if nex not in path and sum(x not in path for x in dic[nex]) == mindgr:
            ret = dfs_extend(dic, path + [nex], n)
            if ret and len(ret) == n:
                return ret

if __name__ == '__main__':
    n = 500
    # path = function(n)
    path = square_sums(n)
    print(n, len(path) == n)
