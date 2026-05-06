def missingNumber(nums):
    expected =0
    actualsum =0
    n = len(nums)
    # for i in range(len(nums)+1):
    #     print(i)
    #     expected +=i

    # for i in nums:
    #     actualsum +=i
    # return expected -actualsum
    expected = n*(n+1)//2
    return expected - sum(nums)
nums =[0,1]
print(missingNumber(nums))