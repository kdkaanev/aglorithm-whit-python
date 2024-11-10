def buble_sort(nums):
    for i in range(len(nums)):
        is_sorted = True
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_sorted = False
        if is_sorted:
            break
    return ' '.join([str(x) for x in nums])


nums = [int(x) for x in input().split()]

print(buble_sort(nums))
