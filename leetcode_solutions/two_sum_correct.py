# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


sol = Solution()
# solA = sol.twoSum([2, 7, 11, 15], 9)  # should return [0, 1]
# print(solA)
solB = sol.twoSum([3, 2, 4], 6)  # should return [1, 2]
print(solB)
# solC = sol.twoSum([3, 3], 6)  # should return [0, 1]
# print(solC)
