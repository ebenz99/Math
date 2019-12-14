class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        dic = {}
        for idx,item in enumerate(groupSizes):
            if item not in dic:
            	dic[item] = []
            dic[item].append(idx)
        res = []
        for key in dic:
        	start = 0
        	while start + key <= len(dic[key]):
        		res.append(dic[key][start:start+key])
        		start += key
        return res

a = Solution()
b = a.groupThePeople([3,1,2,1,3,4,4,3,2,4,4])
print(b)




# groupSizes = [3,3,3,3,3,1,3]
# Output: [[5],[0,1,2],[3,4,6]]

# Input: groupSizes = [2,1,3,3,3,2]
# Output: [[1],[0,5],[2,3,4]]

#[3,1,2,1,3,4,4,3,2,4,4]
#[[1],[3],[2,8],[0,4,7],[5,6,9,10]]