import collections
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #dp with next row being lowest number before this num
        l = len(nums)
        if l < 3:
        	return False
        # a = collections.Counter(nums)
        # if len(a.items()) < 3:
        # 	return False
        # z = 1
        # if 
        # inc = True
        # while z < l:
        # 	if z
        m = max(nums)+1
        dp = [m for num in nums]
        dic = {}

        i = 0
        minNum = m
        while i < l:
        	if minNum < nums[i]:
        		dp[i] = minNum
        		# if minNum not in dic:
        		# 	dic[minNum] = set()
        		# dic[minNum].add(nums[i])
        	if nums[i] < minNum:
        		minNum = nums[i]

        	i+=1

        i = 0
        while i < l:
        	j = i
        	while j < l:
        		if nums[j] > dp[i] and nums[j] < nums[i]:
        			return True
        		j+=1
        	i+=1
       	return False

a = Solution()
b = a.find132pattern([1,1,1,1,1,1,1,4,1,2])
print(b)
