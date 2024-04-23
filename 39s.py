class Solution(object):
    
    def combinationSum(self, candidates, target):
        ans = []

        def dfs(index, cur, total):
            if total == target:
                ans.append(cur.copy())
                return
            if index >= len(candidates) or total > target:
                return
            cur.append(candidates[index])
            dfs(index, cur, total + candidates[index])
            cur.pop()
            dfs(index + 1, cur, total)
        
        dfs(0, [], 0)
        return ans
            

        
x = Solution()
candidates = [2,3,6,7]

print(x.combinationSum(candidates, 7)) # [[2, 2, 3], [7]]




            
        
            

        