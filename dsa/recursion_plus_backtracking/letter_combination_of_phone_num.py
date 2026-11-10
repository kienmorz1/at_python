class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        phone_map = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
        }
        result = []
        def comboMaker(index, current_ans):
            if index == len(digits):
                result.append("".join(current_ans))
                return
            current_digit = digits[index]
            letters = phone_map[current_digit]
            for letter in letters:
                current_ans.append(letter)
                comboMaker(index+1,current_ans)
                current_ans.pop()
        comboMaker(0,[])
        return result

sol = Solution()
print(sol.letterCombinations('23'))