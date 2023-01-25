def find_duplicate(nums):
    if len(nums) <= 1:
        return False
    nums.sort()
    for i in range(len(nums) - 1):
        if type(nums[i]) == str or nums[i] < 0:
            return False
        # if nums[i] < 0:
        #     return False
        if nums[i] == nums[i + 1]:
            return nums[i]
    return False


print(find_duplicate(["guilherme", "felipe"]))
