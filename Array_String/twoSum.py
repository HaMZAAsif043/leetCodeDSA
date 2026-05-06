def twoSum( nums, target):
    seen={}

    for idx, val in enumerate(nums):
            com = target - val
            if com in seen:
                return [seen[com], idx]
            seen[val] = idx

nums = [3,2,4]
target = 6
print(twoSum(nums,target))