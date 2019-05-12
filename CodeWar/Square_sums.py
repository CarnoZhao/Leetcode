def extend_path(dic, path, start):
    for nex in dic[start]:
        if nex not in path:
            return extend_path(dic, path + [nex], nex)
    return path

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


def function(n):
    squares = [x ** 2 for x in range(1, n + 1) if x ** 2 < 2 * n]
    dic = {}
    for num in range(1, n + 1):
        dic[num] = [x - num for x in squares if 0 < x - num <= n and x != 2 * num]
    #     dic[num].append(0)
    # dic[0] = list(range(1, n + 1)
    start = 1
    path = [start]
    path = extend_path(dic, path, start)
    path = extend_path(dic, path[::-1], path[-1])
    for num in dic:
        if num not in path:
            print(num, [x for x in dic[num]])
    print(path)
    print(len(path))

def bfs(n):
    squares = [x ** 2 for x in range(1, n + 1) if x ** 2 < 2 * n]
    dic = {}
    for num in range(1, n + 1):
        dic[num] = [x - num for x in squares if 0 < x - num <= n and x != 2 * num]
        dic[num].append(0)
    dic[0] = list(range(1, n + 1))
    paths = [[0]]
    while paths and len(paths[0]) != n + 1:
        temp = []
        for path in paths:
            for new in dic[path[-1]]:
                if new in path:
                    continue
                temp.append(path + [new])
        paths = temp
        print(len(paths))
    print(paths)

if __name__ == '__main__':
    bfs(40)
    # for n in range(40, 41):
    #     ret = function(n)
    #     if ret:
    #         print(n, ret)
