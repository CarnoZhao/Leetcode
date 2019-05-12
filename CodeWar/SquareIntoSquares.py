def decompose(n):
    ret = dfs(n ** 2, [], n)
    return ret

def dfs(N, arr, n):
    if N == 0:
        return arr 
    for i in range(int(N ** 0.5), 0, -1):
        if i == n or (arr and i >= arr[-1]):
            continue
        ret = dfs(N - i ** 2, arr + [i], n)
        if ret:
            return ret

if __name__ == '__main__':
    n = 50000
    ret = decompose(n)
    print(ret)
