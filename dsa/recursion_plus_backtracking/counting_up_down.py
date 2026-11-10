def bounce(n):
    if n == 0:
        return
        
    print(n)      # Task A: Done on the way "DOWN"
    bounce(n - 1) # Recurse
    print(n)      # Task B: Done on the way "BACK UP" (Backtrack phase)

bounce(3)