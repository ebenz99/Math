import collections
class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        oc = collections.Counter("")
        for word in B:
            nc = collections.Counter(word)
            for letter in nc:
                if letter in oc:
                    oc[letter] = max(oc[letter],nc[letter])
                else:
                    oc[letter] = nc[letter]
        # for key in oc:
        #     mystr+=(key*oc[key])

        universal = []
        for word1 in A:
            word = collections.Counter(word1)
            flag = True
            for key in oc:
                if key not in word:
                    flag = False
                    break
                if oc[key] > word[key]:
                    flag = False
                    break
            if flag == True:
                universal.append(word1)
        return universal


A = ["amazono","apple","facebook","google","leetcode"]
B = ["e","oo","o"]

a = Solution()
print(a.wordSubsets(A,B))