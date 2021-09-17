nums = [2, 5, 7, 1, 0]
for i in range(1, len(nums)):
    for j in range(0, len(nums) - 1):
        if nums[j] > nums[j + 1]:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp
print(nums)