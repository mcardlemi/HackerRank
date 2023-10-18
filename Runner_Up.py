def runnerUp(arr, p):
    if arr[0] > arr[p]:
        return arr[p]
    else:
        return runnerUp(arr, (p+1))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr.reverse()
    print(runnerUp(arr, 0))
