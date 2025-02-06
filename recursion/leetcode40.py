def combinationSum2(candidates, target):
    res = []
    print(len(candidates))
    candidates = sorted(candidates)
    def helper(start, target, stack):

        if target == 0:
            if stack[:] not in res:
                res.append(stack[:])
            return 

        for i in range(start, len(candidates)):
            print(f"choice : {candidates[i]}")
            if candidates[i] <= target:
                stack.append(candidates[i])
                helper(i + 1, target - candidates[i], stack)
                stack.pop()
    
    helper(0, target, [])
    print(res)

# combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 30)