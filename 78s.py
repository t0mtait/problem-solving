class Solution:
    def subsets(self, nums):
        sol = [[]]

        def dfs(i, nums, cur, sol):
            if i == len(nums):
                return
            cur.append(nums[i])
            sol.append(cur.copy())
            dfs(i+1, nums, cur, sol)
            cur.pop()
            dfs(i+1, nums, cur, sol)

        dfs(0, nums, [], sol)
        return sol

x = Solution()
nums = [1,2,3]
print(x.subsets(nums))  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]