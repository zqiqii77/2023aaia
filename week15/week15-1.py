nums=[4,2,5,9,7,4,8]
print(nums)
nums.sort()
print(nums)
print(nums[0], nums[1] )
N=len(nums)
print('長度是', N)
print(nums[N-1],nums[N-2])

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        N=len(nums)

        return nums[N-1]*nums[N-2]-nums[0]*nums[1]