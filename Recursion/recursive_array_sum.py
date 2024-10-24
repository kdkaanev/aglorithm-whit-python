def calculate_sum(num, idx):
    if idx == len(num) - 1:
        return num[idx]
    return num[idx] + calculate_sum(num, idx + 1)

