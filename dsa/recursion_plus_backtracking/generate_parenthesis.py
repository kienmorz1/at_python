class Solution:
    def parentAdd(self, s, open_count, close, ans, n):
        if open_count == close == n:
            ans.append(s)
            return
        if open_count < n:
            self.parentAdd(s+'(', open_count+1, close, ans, n)
        if open_count > close:
            self.parentAdd(s+')', open_count, close+1, ans, n)

    def generateParenthesis(self, n):
        #your code goes here
        ans = []
        self.parentAdd("",0,0,ans,n)
        return ans

sol = Solution()
print(sol.generateParenthesis(2))