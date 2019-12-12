class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        slist = sorted(list(set(nums)), reverse=True)
        pos = {}
        for idx,num in enumerate(nums):
        	if num in pos:
        		pos[num].append(idx)
        	else:
        		pos[num] = [idx]
        subs = [0 for _ in nums]
        for item in slist:
        	print(item)
        	for idx in pos[item]:
	        	spot = idx
	        	i = spot
	        	while i < len(nums):
	        		if nums[i] > item:
	        			subs[spot] = max(subs[i],subs[spot])
	        		i+=1
	        	subs[spot]+=1
        return max(subs)

a = Solution()
b = a.lengthOfLIS([10,9,2,5,3,7,101,18])
b = a.lengthOfLIS([1,2,3,4])
b = a.lengthOfLIS([4,3,2,1])
b = a.lengthOfLIS([1,2,4,3])
b = a.lengthOfLIS([1,2,8,9,3,5,6,7])
print("\n")
print(b)