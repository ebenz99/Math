class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        overallSols = set()
        def twoSum(val,nums):
            dic = {}
            sols = set()
            for num in nums:
                if num in dic:
                    sols.add((num,dic[num]))
                else:
                    dic[val-num] = num
            return sols
        for idx, num in enumerate(nums):
            sols = twoSum(-1*num,nums[:idx]+nums[idx+1:])
            for sol in sols:
                overallSols.add(tuple(sorted((num,sol[0],sol[1]))))
        return list(overallSols)

arr = [1,0,-1,1,6]
a = Solution()

print(a.threeSum(arr))