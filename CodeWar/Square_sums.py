def function(n):
    squares = [x ** 2 for x in range(1, n + 1) if x ** 2 < 2 * n]
    dic = {}
    for num in range(1, n + 1):
        dic[num] = [x - num for x in squares if 0 < x - num <= n and x != 2 * num]
    start = 1
    path = [start]
    path = extend_path_full(dic, path, start)
    path = extend_path_full(dic, path[::-1], path[-1])
    for x in dic[33]:
        print('33`s out: ', x)
        print('next is: ', path[path.index(x) + 1])
        print('linked with: ', dic[path[path.index(x) + 1]])
        print('pre is: ', path[path.index(x) - 1])
        print('linked with: ', dic[path[path.index(x) - 1]])
        print()
    print(path)
    print(len(path))

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

def find_branch(dic, path):
    for i in range(len(path) - 1):
        start, end = path[i:i + 2]
        roots = [[out] for out in dic[start] if out not in path]
        while roots:
            temp = []
            print(roots)
            for root in roots:
                for nex in dic[root[-1]]:
                    print(nex)
                    if nex not in path:
                        temp.append(root + [nex])
                    elif nex == end:
                        return path[:i + 1] + root + path[i + 1:]
            roots = temp
    return path


if __name__ == '__main__':
    for n in range(40, 41):
        ret = function(n)
        if ret:
            print(n, ret)
