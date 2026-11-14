def partition_string(s):
    result = []
    
    def backtrack(index, current_slices):
        # -----------------------------------------------
        # YOUR LOGIC 1: Base Case (Reached the end)
        # -----------------------------------------------
        if index == len(s):
            result.append(list(current_slices))
            return
            
        # -----------------------------------------------
        # LOGIC 2: Loop to try different slice lengths
        # i goes from our current position to the very end
        # -----------------------------------------------
        for i in range(index, len(s)):
            # Take the slice from 'index' up to 'i + 1'
            # e.g., if s="123" and index=0:
            # i=0 -> slice is "1"
            # i=1 -> slice is "12"
            # i=2 -> slice is "123"
            current_slice = s[index : i + 1]
            
            # 1. Make choice
            current_slices.append(current_slice)
            
            # 2. Recurse forward starting right AFTER our cut (i + 1)
            backtrack(i + 1, current_slices)
            
            # 3. Backtrack (Undo the cut)
            current_slices.pop()

    backtrack(0, [])
    return result

print(partition_string("123"))
# Output: [['1', '2', '3'], ['1', '23'], ['12', '3'], ['123']]
