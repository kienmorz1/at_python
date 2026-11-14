class Solution(object):
    def sumIdentifier(self, k, n):
        result = []
        
        def identifier(current_sum, current_combo, current_num):
            # --------------------------------------------------
            # BASE CASE 1: SUCCESS! (Exactly k items and matches target)
            # --------------------------------------------------
            if len(current_combo) == k and current_sum == n:
                result.append(list(current_combo)) # Take a snapshot
                return
                
            # BASE CASE 2: STOP CONDITONS (Overshot sum, too many items, or past 9)
            if current_sum > n or len(current_combo) > k or current_num > 9:
                return

            # --------------------------------------------------
            # CHOICE A: "TAKE IT" (Your original logic)
            # --------------------------------------------------
            current_combo.append(current_num)
            # Recurse forward with updated sum and next number
            identifier(current_sum + current_num, current_combo, current_num + 1)
            
            # THE BACKTRACK STEP: Undo Choice A
            current_combo.pop() 

            # --------------------------------------------------
            # CHOICE B: "LEAVE IT" (Skip this number entirely)
            # --------------------------------------------------
            # Recurse forward WITHOUT adding current_num to sum or combo
            identifier(current_sum, current_combo, current_num + 1)

        # Start the engine
        identifier(0, [], 1)
        return result
      

sol = Solution()
print(sol.sumIdentifier(3,7))