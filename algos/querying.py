import re
class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        res = []
        vowels=b'aeiouAEIOU'
        dic={}
        wset = set(wordlist)
        overallDict = {}
        for letter in vowels:
            dic[letter] = '?'
        for word in queries:
            found = False
            if word in wset:
                res.append(word)
                found = True
                continue
            lword = word.lower()
            if found == False:
                for word2 in wordlist:
                    if found == True:
                        break
                    if lword == word2.lower():
                        res.append(word2)
                        found = True
            if found == False:
                #qword = word.translate(str.maketrans(dic)).lower()
                qword = re.sub(r'[AEIOUaeiou]', '?', word).lower()
                for word2 in wordlist:
                    if found == True:
                        break
                    if word2 not in overallDict:
                        #overallDict[word2] = word2.translate(str.maketrans(dic)).lower()
                        overallDict[word2] = re.sub(r'[AEIOUaeiou]', '?', word2).lower()
                    if qword == overallDict[word2]:
                        res.append(word2)
                        found = True
                        break
            if found == False:
                res.append("")
        return res
wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
a = Solution()
print(a.spellchecker(wordlist,queries))