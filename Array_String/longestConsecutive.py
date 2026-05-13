def longestConsecutive(nums):
        if len(nums) ==0 :
                return 0
        sorted_array = sorted(nums)

        current =1
        max_ret=1
        for i in range(0,len(sorted_array)-1):

            if sorted_array[i+1] == sorted_array[i]:
                continue
            elif sorted_array[i+1] == sorted_array[i] + 1:
                current += 1
            else: 
                max_ret = max(max_ret, current)
                current = 1
        return max(max_ret, current)   


nums = [0,3,2,5,4,6,1,1]
print(longestConsecutive(nums))