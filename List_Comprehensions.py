if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    cuboid = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if not (i+j+k==n)]
    print(cuboid)
