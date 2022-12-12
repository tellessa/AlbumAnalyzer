# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution:
    def twoSum(self, nums, target):
        # TODO: return as soon as we find one solution
        for num in nums:
            # compare to all other nums
            other_nums = nums.copy()
            other_nums.remove(num)
            # TODO: rather than iterating blindly through possible complements,
            # It's better to use a sorted array
            other_nums.sort()
            # for possible_complement in other_nums:
            # binary search
            middle = int((len(other_nums)/2))
            possible_complement = other_nums.pop(middle)
            if num + possible_complement == target:
                # Base case
                # TODO: make this work for duplicate pairs, ie 3, 3
                true_num_index = nums.index(num)
                true_complement_index = nums.index(possible_complement, true_num_index+1)
                return [true_num_index, true_complement_index]
            elif num + possible_complement > target:
                # recursive case
                middle = int((len(other_nums)/2))
                possible_complement = other_nums.pop(middle)
            else:
                pass
                # recursive case: num + possible_complement < target

                # TODO: 55/57 testcases pass


sol = Solution()
# solA = sol.twoSum([2, 7, 11, 15], 9)  # should return [0, 1]
# print(solA)
solB = sol.twoSum([3, 2, 4], 6)  # should return [1, 2]
print(solB)
# solC = sol.twoSum([3, 3], 6)  # should return [0, 1]
# print(solC)


# The last two numbers add up to the target.
# TODO: Add a check to make sure we only compare to numbers that are...
# As a human being I can see the sequence of the numbers in the second to last example
# I see they are increasing and therefore I know the ones at the end have the greatest chance of meeting the target
# If we sorted them first, we could also make sure they are meeting the target
# The modified .index call will still find us the original index even if we sort on our separate working copy.
# We need some variation of binary search
