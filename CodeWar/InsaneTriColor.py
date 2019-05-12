def insane_tri_bicolor_tiling(n, r, g, b):
    colors = ((r, g), (g, b), (r, b))
    ret = 0
    for color in colors:
        c1, c2 = color
        global_pre = 1
        x = 0
        while (x + 1) * c1 <= n:
            z = n - x * c1
            global_pre = global_pre * pi([z - i for i in range(c1)]) // (x + 1) // pi([x + z - c1 + i for i in range(2, c1 + 1)])
            local_pre = global_pre
            x += 1
            y = 0
            while x * c1 + (y + 1) * c2 <= n:
                z = n - x * c1 - y * c2
                local_pre = local_pre * pi([z - i for i in range(c2)]) // (y + 1) // pi([x + y + z - c2 + i for i in range(2, c2 + 1)])
                y += 1
                ret = (ret + local_pre) % 12345787
    return int(ret)

def pi(nums):
    ret = 1
    for num in nums:
        ret *= num
    return ret

if __name__ == '__main__':
    ret = insane_tri_bicolor_tiling(100, 2, 3, 4)
    print(ret)
