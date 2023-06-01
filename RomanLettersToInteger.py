class Solution(object):
    def __init__(self):
        self.dict = {}
        self.dict["I"] = 1
        self.dict["V"] = 5
        self.dict["X"] = 10
        self.dict["L"] = 50
        self.dict["C"] = 100
        self.dict["D"] = 500
        self.dict["M"] = 1000
        
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        integer = 0
        for i in range(len(s)-1):
            if self.dict[s[i]] < self.dict[s[(i+1)]]:
                integer-=self.dict[s[i]] 
            else:
                integer+=self.dict[s[i]]
        return integer+self.dict[s[-1]]
s = "III"
d = Solution()
print(d.romanToInt(s))
