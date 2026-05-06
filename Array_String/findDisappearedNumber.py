# def findDisappearedNumbers(nums):
#         n = len(nums)
#         expected_sum =n*(n+1)//2 
#         actualSum= 0
#         result = dict()
#         for i in range(n):
#             if i in result:
#                 pass
#             result[nums[i]] =True
#             actualSum +=nums[i]
#             print(f'Iteration {i} value in actualSUm {actualSum},{nums[i]}')
#         print(expected_sum,actualSum,result)
#         missing = expected_sum -actualSum
#         return (missing)
def findDisappearedNumbers(nums):
    n = len(nums)
    present = set(nums)
    return [i for i in range(1, n+1) if i not in present]
nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))


    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     arr = [0]*(len(nums) + 1)
    #     ans = []
    #     for n in nums:
    #         arr[n] = 1
    #     for i in range(1, len(arr)):
    #         if arr[i] == 0:
    #             ans.append(i)
    #     return ans
        