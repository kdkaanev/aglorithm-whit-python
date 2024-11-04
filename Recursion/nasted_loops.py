def nasted_loops(idx, arr):
    if idx >= len(arr):
        print(*arr, sep=' ')
        return
    for num in range(1, len(arr) + 1):
        arr[idx] = num
        nasted_loops(idx + 1, arr)


n = int(input())
arr = [None] * n

nasted_loops(0, arr)
