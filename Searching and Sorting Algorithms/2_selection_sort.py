def sort_selection(nums):
    for i in range(len(nums)):
        for cur_index in range(i + 1, len(nums)):
            if nums[cur_index] < nums[i]:
                nums[cur_index], nums[i] = nums[i], nums[cur_index]
    return ' '.join([str(x) for x in nums])


nums = [int(x) for x in input().split()]

print(sort_selection(nums))
