class Solution:  
    def power(self,x,n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2:
            return x * self.power(x,n-1)
        else:
            return self.power(x*x, n//2)  
    def myPow(self, x, n):
        #your code goes here
        num = n
        if num < 0:
            return 1.0/self.power(x,-num)
        return self.power(x,num)

sol = Solution()
print(sol.myPow(2,10))