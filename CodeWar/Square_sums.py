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
        dic[num].append(0)
    dic[0] = list(range(1, n + 1))
    start = 1
    path = [0, 1]
    path = extend_path_full(dic, path, start)
    # path = extend_path_full(dic, path[::-1], path[-1])
    outs = [out for out in dic if out not in path]
    # print(outs)
    positions = dict((node, i) for i, node in enumerate(path))
    # for out in outs:
    #     for start in path:
    #         if start not in dic[out]:
    #             continue
    #         starts = [[start]]
    #         used = {start}
    #         while all(x not in [x[-1] for x in starts] for x in dic[out] if x != start):
    #             temp = []
    #             for start in starts:
    #                 right_one = path[(positions[start[-1]] + 1) % len(path)]
    #                 right_two = [x for x in dic[right_one] if x in path and positions[x] not in [positions[right_one] + 1, positions[right_one], positions[right_one] - 1]]
    #                 for new in right_two:
    #                     new = path[positions[new] - 1]
    #                     if new not in used:
    #                         used.add(new)
    #                         temp.append(start + [new])
    #             starts = temp
    #         if any(x in [x[-1] for x in starts] for x in dic[out] if x != start):
    #             break
    #     rotate = [x for x in starts if x[-1] in dic[out]][0]
    #     print(rotate)
    print(path)
    # print(len(path))
    return path

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
    # for path in paths:
    #     print(', '.join(str(x) for x in path))
    #     print()
    return paths

def dfs(n):
    squares = [x ** 2 for x in range(1, n + 1) if x ** 2 < 2 * n]
    dic = {}
    for num in range(1, n + 1):
        dic[num] = [x - num for x in squares if 0 < x - num <= n and x != 2 * num]
        dic[num].append(0)
    dic[0] = list(range(1, n + 1))
    path = dfs_extend(dic, [0])
    return path

def dfs_extend(dic, path):
    for nex in dic[path[-1]]:
        if nex not in path:
            ret = dfs_extend(dic, path + [nex])
            if ret and len(ret) == n + 1:
                return ret
    return path if len(path) == n + 1 else None

if __name__ == '__main__':
    n = 39
    print(dfs(n))
    # paths = bfs(n)
    # print(paths)
    path = function(n)
    # maxcor = 0
    # maxp = []
    # for p in paths:
    #     correct = max(sum(x == y for x, y in zip(p, path[i:] + path[:i])) for i in range(len(path)))
    #     if correct > maxcor:
    #         maxcor = correct
    #         maxp = p
    # print(str(maxp)[1:-1])
    # print(str(path)[1:-1])
