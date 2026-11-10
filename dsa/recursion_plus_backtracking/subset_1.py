class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def ss(index,current_ans):
            if index == len(nums):
                result.append(list(current_ans))
                return
            current_ans.append(nums[index])
            ss(index+1,current_ans)
            current_ans.pop()
            ss(index+1,current_ans)
        ss(0,[])

sol = Solution()
print(sol.subsets([1,2,3]))