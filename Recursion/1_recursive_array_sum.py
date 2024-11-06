def calculate_sum(num, idx):
    if idx == len(num) - 1:
        return num[idx]
    return num[idx] + calculate_sum(num, idx + 1)


num = [int(x) for x in input().split()]
print(calculate_sum(num, 0))
