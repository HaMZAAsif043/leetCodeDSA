def smallerNumbersThanCurrent(nums) :
        temp = sorted(nums)
        res ={}
        for i ,val in enumerate(temp):
            if val not in res:
                res[val]=i
        ret =[]
        print(res)
        for i in nums:
            ret.append(res[i])

        return ret
nums=[8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))