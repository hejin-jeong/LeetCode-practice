class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        # mapper=["0","1","abc","def","ghi", "jkl","mno","pqrs","tuv","wxyz"]
        res= []
        
        if not digits:
            return res
        
        res.append("")
        
        for digit in digits:
            temp=list()
            chars = phone[digit]
            for r in res:
                for cha in chars:
                    temp.append(r+cha)
                    
            res = temp
        return res