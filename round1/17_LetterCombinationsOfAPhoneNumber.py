class Solution(object):
    def letterCombinations(self, digits):
        dic = {'1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':' '}
        a = ['']
        o = []
        for i in digits:
            o = []
            for j in a:
                for k in dic[i]:
                    o.append(j+k)
            a = o[:]
        return o
            
        """
        :type digits: str
        :rtype: List[str]
        """