class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        mappings = {}
        i = 0
        l = len(nums)
        while i < l:
        	ogNextSpot = nums[i]
        	nextSpot = ogNextSpot
        	seen.add(i)
        	counter = 1
        	while nextSpot < l and nextSpot not in seen:
        		seen.add(nextSpot)
        		nextSpot = nums[nextSpot]
        		counter+=1
        	if nextSpot in mappings:
        		mappings[ogNextSpot] = mappings[nextSpot] + counter
        	else:
        		mappings[ogNextSpot] = counter
        	i+=1
        return max(mappings.items(), key = lambda kv: kv[1])[1]



a = Solution()
print(a.arrayNesting([5,4,0,3,1,6,2]))