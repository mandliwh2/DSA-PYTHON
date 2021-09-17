nums = [3, 7, 9, 1, 2]
x = []
for j in range(len(nums)):
    minNum = nums[0]
    for i in nums:
        if i <= minNum:
            minNum = i
    x.append(minNum)
    nums.remove(minNum)
print(x)

