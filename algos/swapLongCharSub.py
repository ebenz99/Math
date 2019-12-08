class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        # tb = [None, 0, False]
        # ob = [None, 0, False]
        # m = [None, 0]
        # graceUsed = False
        # replaced = False
        # for idx, letter in enumerate(text):
        #     if letter == ob[0]:
        #         ob[1]+=1
        #         if tb[2] == True:
        #             tb = [tb[0],1,False]
        #             print(tb,ob,letter)
        #         else:
        #             tb[2] =True
        #             print(tb,ob,letter)
        #     elif letter == tb[0]:
        #         if tb[2] == False:
        #             past = ob
        #             ob = list(tb)
        #             tb = list(past)
        #             ob[2] = True
        #             ob[1] += 1
        #             print(tb,ob,letter)
        #         else:
        #             tb = list(ob)
        #             ob = [letter,1, False]
        #             print(tb,ob,letter)
        #     else:
        #         tb = list(ob)
        #         ob = [letter,1,False]
        #         print(tb,ob,letter)
        #     m = max(m,ob[:2], key = lambda kv: kv[1])
        #     #print(m)
        # if text.count(m[0]) > m[1]:
        #     m[1]+=1
        # return m[1]
        m = [None,0]
        i = 0
        backTo = 0
        while i < len(text)-1:
            #print(i)
            j = i+1
            counter = 1
            graced = 0
            curr = text[i]
            while j < len(text):
                if text[j] == curr:
                    counter+=1
                    # if counter == 4:
                    #     print("j is %d" % j)
                else:
                    if graced == 1:
                        break
                    counter += 1
                    graced = 1
                    backTo = j
                #print(curr,j,text[j],counter)
                j+=1
            m = max([curr,counter],m, key = lambda kv: kv[1])
            #print(backTo)
            if j >= len(text):
                break
            else:
                i = backTo
        return min(m[1],text.count(m[0]))

a = Solution()
print(a.maxRepOpt1("aabaaabaaabacccccccccc"))
