def binary_search(nums, target):
    left_idx = 0
    right_idx = len(nums) - 1
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        mid = nums[mid_idx]
        if mid == target:
            return mid_idx
        if mid < target:
            left_idx = mid_idx + 1
        else:

            right_idx = mid_idx - 1

    return -1


nums = [int(x) for x in input().split()]
target = int(input())

print(binary_search(nums, target))
