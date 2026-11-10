class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        def ss(index,current_ans):
            if index == len(nums):
                result.append(list(current_ans))
                return
            current_ans.append(nums[index])
            ss(index+1, current_ans)
            current_ans.pop()
            next_index = index + 1
            while next_index < len(nums) and nums[next_index] == nums[index]:
                next_index += 1
            ss(next_index, current_ans)
        ss(0,[])
        return result

sol = Solution()
print(sol.subsetsWithDup([1,2,2,3]))